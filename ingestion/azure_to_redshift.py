from azure.storage.blob import BlobClient
import pandas as pd
from io import StringIO
import configparser
import logging
import json
import psycopg2


try:
    with open("ingestion/configuration.json") as json_credentials_file:
        credentials = json.load(json_credentials_file)
except Exception:
    print("Configuration file doesn't exist")

config = configparser.ConfigParser()
config.read_file(open("ingestion/config.cfg"))


def azure_to_redshift_func():
    blobs = [
        BlobClient(account_url=credentials["account_url"],
                   container_name=credentials['cantainer_name'],
                   blob_name=credentials["candidate"],
                   credential=credentials["credential"]),

        BlobClient(account_url=credentials["account_url"],
                   container_name=credentials['cantainer_name'],
                   blob_name=credentials["offers"],
                   credential=credentials["credential"]),

        BlobClient(account_url=credentials["account_url"],
                   container_name=credentials['cantainer_name'],
                   blob_name=credentials["demographics"],
                   credential=credentials["credential"])]

    data = [blob.download_blob() for blob in blobs]

    dfs = [pd.read_csv(StringIO(data[0].content_as_text()), sep=";"), pd.read_csv(StringIO(
        data[1].content_as_text()), sep=";"), pd.read_csv(StringIO(data[2].content_as_text()), sep=";")]

    conn = psycopg2.connect(
        host=config.get("AWS", "host"),
        port=config.get("AWS", "port"),
        dbname=config.get("AWS", "dbname"),
        user=config.get("AWS", "user"),
        password=config.get("AWS", "password"))

    cur = conn.cursor()

    # data to be loaded
    candidate_df = dfs[0].drop("practice_name", axis=1)
    offers_df = dfs[1]
    demographics_df = dfs[2]

    for i, row in candidate_df.iterrows():
        cur.execute(
            "INSERT INTO public.candidates VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", list(row))
        conn.commit()

    for i, row in offers_df.iterrows():
        cur.execute(
            "INSERT INTO public.offers VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", list(row))
        conn.commit()

    # for i, row in demographics_df.iterrows():
        # cur.execute(
        #   "INSERT INTO public.demographics VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", list(row))
        # conn.commit()

    # print("finished")

    return True
