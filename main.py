from configurator import ETLConfigurator


def main(params):
    configurator = ETLConfigurator(config=params)
    etl = configurator.etl()
    etl.run()


if __name__ == '__main__':
    config = {
        'module': 'etl',

        'extractor': 'SimpleExtractor',
        'loader': 'SimpleLoader',
        'ETL': 'HelloWorldETL',

        'parameters': {'k': 10},
        'loader-config': {'api_key': 123}

    }

    main(params=config)
