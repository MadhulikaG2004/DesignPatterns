class HttpRequest:
    def __init__(self,builder):
        self.url=builder.url
        self.method=builder._method
        self.headers=dict(builder._headers)
        self.query_params=dict(builder._query_params)
        self.body = builder._body
        self.timeout = builder._timeout
    class Builder:
        def __init__(self,url):
            self._url = url  # required
            self._method = "GET"
            self._headers = {}
            self._query_params = {}
            self._body = None
            self._timeout = 30000
        def method(self,method):
            self._method=method
            return self
        def add_header(self,key,value):
            self._headers[key]=value
            return self
        def add_query_param(self,key,value):
            self._query_params[key]=value
            return self
        def body(self,body):
            self._body=body
            return self 
        def timeout(self,timeout):
            self._timeout=timeout
            return self
        def build(self):
            return self
if __name__ == "__main__":
    # Simple GET request
    get = HttpRequest.Builder("https://api.example.com/users") \
        .build()

    # POST with body and custom timeout
    post = HttpRequest.Builder("https://api.example.com/users") \
        .method("POST") \
        .add_header("Content-Type", "application/json") \
        .body('{"name":"Alice","email":"alice@example.com"}') \
        .timeout(5000) \
        .build()

    # Authenticated PUT with query parameters
    put = HttpRequest.Builder("https://api.example.com/config") \
        .method("PUT") \
        .add_header("Authorization", "Bearer token123") \
        .add_header("Content-Type", "application/json") \
        .add_query_param("env", "production") \
        .add_query_param("version", "2") \
        .body('{"feature_flag":true}') \
        .timeout(10000) \
        .build()

    print(get)
    print(post)
    print(put)