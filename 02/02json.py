import jsonpath
dict = {
  "store": {
    "book": [
      {
        "category": "classics",
        "author": "施耐庵",
        "title": "水浒传",
        "price": 58.00
      },
      {
        "category": "classics",
        "author": "罗贯中",
        "title": "三国演义",
        "price": 68.00
      },
      {
        "category": "classics",
        "author": "吴承恩",
        "title": "西游记",
        "isbn": "978-7-5327-6543-2",
        "price": 78.00
      },
      {
        "category": "classics",
        "author": "曹雪芹",
        "title": "红楼梦",
        "isbn": "978-7-5302-1843-4",
        "price": 88.00
      }
  ]
    }
}
print(jsonpath.jsonpath(dict,'$.store.book[*].author'))
print(jsonpath.jsonpath(dict,'$..author'))












