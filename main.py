import src.companiesdb as comp
import src.google_api_requests as google


def main():
    db, offices = comp.connectCollection('companies', 'offices')
    target = comp.target_offices(offices, 'USA', 2009, 1)
    result, df = comp.offices_filter(target, offices)


if __name__ == "__main__":
    main()
