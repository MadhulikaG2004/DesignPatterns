from abc import ABC,abstractmethod
import time
class ApiService(ABC):
    def request(self,endpoint:str):
        pass

class RealApiService(ApiService):
    def request(self, endpoint):
        return f"processing {endpoint}"

class ApiServiceProxy(ApiService):
    MAX_REQUESTS = 3
    TIME_WINDOW = 10

    def __init__(self,real_api_service: ApiService):
        self._api_service=real_api_service
        self._timestamps=[]
    def request(self,endpoint):
        ti=time.time()
        self._timestamps=[t for t in self._timestamps if ti-t<=self.TIME_WINDOW]
        if len(self._timestamps)>=self.MAX_REQUESTS:
            print("Rate limit exceeded!")
        self._timestamps.append(ti)
        result=self._api_service.request(endpoint)
        return result

if __name__=="__main__":
    api= ApiServiceProxy(RealApiService())
    print(api.request("/users"))
    print(api.request("/orders"))
    print(api.request("/products"))
    print(api.request("/inventory")) 