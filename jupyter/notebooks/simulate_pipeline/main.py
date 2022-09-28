from config import My_Config as cfg
from extract import Get_billing
from combine import Combine


def extract():
    print("Extracting data")
    Get_billing.azure_billing()
    Get_billing.aws_billing()
    Get_billing.gcp_billing()
    print("Extraction complete")

def combine():
    print("Deviding data")
    table = cfg.storage_blob_name()
    Combine.main(table)
    print("Data combined")

def main():
    extract()
    combine()
    


if __name__ == '__main__':
    main()