# Redis

## Simple Dynamic String 简单动态字符串

SDS，简单动态字符串。

二进制安全，O1获得长度，不仅仅存储字符串，惰性释放，预分配 。

```c
struct sdshdr {
    int len;
    int free;
    char buff[];
}
```

## 链表


## 对象

会有一层对象封装来封装底层数据。
```c
#define LRU_BITS 24
typedef struct redisObject { 
    unsigned type:4;
    unsigned encoding:4;
    unsigned lru:LRU_BITS; /* LRU time (relative to global lru_clock) or
                            * LFU data (least significant 8 bits frequency
                            * and most significant 16 bits access time). */
    int refcount;
    void *ptr;
} robj;
```

### type是字符串
encoding类型有embstr，row，int
int的字符串对象可以使用引用计数。
embstr是申请robj的时候一起申请sds内存，节省malloc申请释放次数和提高缓存效率。
```c
/* Create a string object with EMBSTR encoding if it is smaller than
 * OBJ_ENCODING_EMBSTR_SIZE_LIMIT, otherwise the RAW encoding is
 * used.
 *
 * The current limit of 44 is chosen so that the biggest string object
 * we allocate as EMBSTR will still fit into the 64 byte arena of jemalloc. */
#define OBJ_ENCODING_EMBSTR_SIZE_LIMIT 44
robj *createStringObject(const char *ptr, size_t len) {
    if (len <= OBJ_ENCODING_EMBSTR_SIZE_LIMIT)
        return createEmbeddedStringObject(ptr,len);
    else
        return createRawStringObject(ptr,len);
}
```
44 = 64 - sizeof(redisObject):16 - sizeof(sdshdr8):4

## 数据库结构
```c
struct redisServer {
    redisDb *db;
} # db数组
struct redisClient {
    redisDb *db;
} # 指向Server
struct redisDb {
    dict *dict;
} # 存储redisObject的KV哈希字典
```