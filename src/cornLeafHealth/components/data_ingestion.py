# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 14:02:12 2024

@author: Dobrucki
"""

import os
import zipfile
import gdown
from cornLeafHealth import logger
from cornLeafHealth.utils.common import get_size
from cornLeafHealth.entity.config_entity import (DataIngestionConfig)

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        
    def download_file(self) -> str:
        
        try:
            url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.info(f"Downloading data from {url} into file {zip_download_dir}")
            file_id = url.split("/")[-2]
            prefix_url = "https://drive.google.com/uc?/export=download&id="
            gdown.download(prefix_url+file_id, zip_download_dir)
            logger.info(f"Downloaded data from {url} into file {zip_download_dir}")
        
        except Exception as e:
            raise e
            

    def extract_zip(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)