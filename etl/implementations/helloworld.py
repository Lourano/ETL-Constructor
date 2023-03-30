from ..structure import ETL


class HelloWorldETL(ETL):
    def transform(self, data):
        print("Transforming...")
        return {
            k: data.count(k) for k in set(data)
        }
