import os

ENV = os.getenv("ENV", "QA")

ENV_CONFIG = {
    "QA": { 
        "BASE_URL" :  "https://opensource-demo.orangehrmlive.com",
        "SCHOOL_ID" : None,
        "USERNAME" : "Admin",
        "PASSWORD" :"admin123",
        },   
    "STAGE": {
        "BASE_URL" : "https://stage.orangehrmlive.com",
        "USERNAME" : "StageAdmin",
        "PASSWORD" : "admin123", 
    },
    "PROD": {
        "BASE_URL" : "https://prod.orangehrm.com",
        "USERNAME" : "ProdAdmin",
        "PASSWORD" : "prod123",
        },
        "Team5": {
            "BASE_URL": "https://mis-teams-team5.bromcom.dev/",
            "SCHOOL_ID": "851171",
            "USERNAME": "brcm",
            "PASSWORD": "Br0mc0m_1234",
        },
        "Release": {
            "BASE_URL": "https://mis-release.bromcom.dev/",
            "SCHOOL_ID": "311391",
            "USERNAME" : "brcm",
            "PASSWORD" : "Br0mc0m_1234",
        },
        "Hotfix" : {
            "BASE_URL" : "https://mis-hotfix.bromcom.dev/",
            "SCHOOL_ID" : "611391",
            "USERNAME" : "brcm",
            "PASSWORD" : "Br0mc0m_1234",
        }
}

# Final selected environment configuration
CONFIG = ENV_CONFIG[ENV]

BASE_URL = CONFIG["BASE_URL"]
SCHOOL_ID = CONFIG["SCHOOL_ID"]
USERNAME = CONFIG["USERNAME"]
PASSWORD = CONFIG["PASSWORD"]
DEFAULT_TIMEOUT = 10000  # 10 seconds