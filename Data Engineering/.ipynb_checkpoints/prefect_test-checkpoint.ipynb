{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ce2e17c5-e5f1-4114-aaf0-c888e234ca6b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "C:\\Users\\USER PC\\prefect_env\\Scripts\\python.exe\n"
     ]
    }
   ],
   "source": [
    "import sys\n",
    "print(sys.executable)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "90fc815f-b1c1-403e-ad50-781a0dba383c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'3.6.2'"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import prefect\n",
    "\n",
    "prefect.__version__\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "8bc1f693-b023-45a6-b457-05a0bb706d3b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "\n",
    "os.environ[\"PREFECT_API_URL\"] = \"https://api.prefect.cloud/api/accounts/5a41b131-4cbc-419c-9685-bef0b843bc45/workspaces/e31d45fa-dde7-4d90-9e9c-6489ae12e97f\"\n",
    "os.environ[\"PREFECT_API_KEY\"] = \"e2ff8e020abb574b3f2eb97c686b2ba6\"\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e2f32117-ae53-42d0-95e6-966a3b824778",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "API URL: https://api.prefect.cloud/api/accounts/5a41b131-4cbc-419c-9685-bef0b843bc45/workspaces/e31d45fa-dde7-4d90-9e9c-6489ae12e97f\n",
      "API KEY set? : YES\n"
     ]
    }
   ],
   "source": [
    "from prefect.settings import PREFECT_API_URL, PREFECT_API_KEY\n",
    "\n",
    "print(\"API URL:\", PREFECT_API_URL.value())\n",
    "print(\"API KEY set? :\", \"YES\" if PREFECT_API_KEY.value() else \"NO\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "986b66bf-6410-4883-956e-9b612b1415e5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Cabin</th>\n",
       "      <th>Embarked</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Braund, Mr. Owen Harris</td>\n",
       "      <td>male</td>\n",
       "      <td>22.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>A/5 21171</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>\n",
       "      <td>female</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>PC 17599</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>C85</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>Heikkinen, Miss. Laina</td>\n",
       "      <td>female</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>STON/O2. 3101282</td>\n",
       "      <td>7.9250</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>\n",
       "      <td>female</td>\n",
       "      <td>35.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>113803</td>\n",
       "      <td>53.1000</td>\n",
       "      <td>C123</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Allen, Mr. William Henry</td>\n",
       "      <td>male</td>\n",
       "      <td>35.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>373450</td>\n",
       "      <td>8.0500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   PassengerId  Survived  Pclass  \\\n",
       "0            1         0       3   \n",
       "1            2         1       1   \n",
       "2            3         1       3   \n",
       "3            4         1       1   \n",
       "4            5         0       3   \n",
       "\n",
       "                                                Name     Sex   Age  SibSp  \\\n",
       "0                            Braund, Mr. Owen Harris    male  22.0      1   \n",
       "1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   \n",
       "2                             Heikkinen, Miss. Laina  female  26.0      0   \n",
       "3       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1   \n",
       "4                           Allen, Mr. William Henry    male  35.0      0   \n",
       "\n",
       "   Parch            Ticket     Fare Cabin Embarked  \n",
       "0      0         A/5 21171   7.2500   NaN        S  \n",
       "1      0          PC 17599  71.2833   C85        C  \n",
       "2      0  STON/O2. 3101282   7.9250   NaN        S  \n",
       "3      0            113803  53.1000  C123        S  \n",
       "4      0            373450   8.0500   NaN        S  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "train = pd.read_csv(\"train.csv\")\n",
    "train.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "a8507dae-5d02-4a95-82b5-ca229f31fa36",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">09:13:55.072 | <span style=\"color: #008080; text-decoration-color: #008080\">INFO</span>    | Flow run<span style=\"color: #800080; text-decoration-color: #800080\"> 'silver-uakari'</span> - Beginning flow run<span style=\"color: #800080; text-decoration-color: #800080\"> 'silver-uakari'</span> for flow<span style=\"color: #800080; text-decoration-color: #800080; font-weight: bold\"> 'elt-titanic-flow'</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "09:13:55.072 | \u001b[36mINFO\u001b[0m    | Flow run\u001b[35m 'silver-uakari'\u001b[0m - Beginning flow run\u001b[35m 'silver-uakari'\u001b[0m for flow\u001b[1;35m 'elt-titanic-flow'\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">09:13:55.086 | <span style=\"color: #008080; text-decoration-color: #008080\">INFO</span>    | Flow run<span style=\"color: #800080; text-decoration-color: #800080\"> 'silver-uakari'</span> - View at <span style=\"color: #0000ff; text-decoration-color: #0000ff\">https://app.prefect.cloud/account/5a41b131-4cbc-419c-9685-bef0b843bc45/workspace/e31d45fa-dde7-4d90-9e9c-6489ae12e97f/runs/flow-run/06922981-1c83-734f-8000-155435dc07df</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "09:13:55.086 | \u001b[36mINFO\u001b[0m    | Flow run\u001b[35m 'silver-uakari'\u001b[0m - View at \u001b[94mhttps://app.prefect.cloud/account/5a41b131-4cbc-419c-9685-bef0b843bc45/workspace/e31d45fa-dde7-4d90-9e9c-6489ae12e97f/runs/flow-run/06922981-1c83-734f-8000-155435dc07df\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">09:13:56.375 | <span style=\"color: #008080; text-decoration-color: #008080\">INFO</span>    | Task run 'extract_train-4bb' - Extracted 891 rows from train.csv\n",
       "</pre>\n"
      ],
      "text/plain": [
       "09:13:56.375 | \u001b[36mINFO\u001b[0m    | Task run 'extract_train-4bb' - Extracted 891 rows from train.csv\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">09:13:56.384 | <span style=\"color: #008080; text-decoration-color: #008080\">INFO</span>    | Task run 'extract_train-4bb' - Finished in state <span style=\"color: #008000; text-decoration-color: #008000\">Completed</span>()\n",
       "</pre>\n"
      ],
      "text/plain": [
       "09:13:56.384 | \u001b[36mINFO\u001b[0m    | Task run 'extract_train-4bb' - Finished in state \u001b[32mCompleted\u001b[0m()\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">09:13:58.183 | <span style=\"color: #008080; text-decoration-color: #008080\">INFO</span>    | Task run 'load_raw-318' - Loaded raw data into table 'titanic_raw'\n",
       "</pre>\n"
      ],
      "text/plain": [
       "09:13:58.183 | \u001b[36mINFO\u001b[0m    | Task run 'load_raw-318' - Loaded raw data into table 'titanic_raw'\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">09:13:58.199 | <span style=\"color: #008080; text-decoration-color: #008080\">INFO</span>    | Task run 'load_raw-318' - Finished in state <span style=\"color: #008000; text-decoration-color: #008000\">Completed</span>()\n",
       "</pre>\n"
      ],
      "text/plain": [
       "09:13:58.199 | \u001b[36mINFO\u001b[0m    | Task run 'load_raw-318' - Finished in state \u001b[32mCompleted\u001b[0m()\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">09:14:00.108 | <span style=\"color: #008080; text-decoration-color: #008080\">INFO</span>    | Task run 'transform_in_db-ac9' - Transform step completed inside MySQL (titanic_clean filled)\n",
       "</pre>\n"
      ],
      "text/plain": [
       "09:14:00.108 | \u001b[36mINFO\u001b[0m    | Task run 'transform_in_db-ac9' - Transform step completed inside MySQL (titanic_clean filled)\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">09:14:00.132 | <span style=\"color: #008080; text-decoration-color: #008080\">INFO</span>    | Task run 'transform_in_db-ac9' - Finished in state <span style=\"color: #008000; text-decoration-color: #008000\">Completed</span>()\n",
       "</pre>\n"
      ],
      "text/plain": [
       "09:14:00.132 | \u001b[36mINFO\u001b[0m    | Task run 'transform_in_db-ac9' - Finished in state \u001b[32mCompleted\u001b[0m()\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">09:14:00.535 | <span style=\"color: #008080; text-decoration-color: #008080\">INFO</span>    | Flow run<span style=\"color: #800080; text-decoration-color: #800080\"> 'silver-uakari'</span> - Finished in state <span style=\"color: #008000; text-decoration-color: #008000\">Completed</span>()\n",
       "</pre>\n"
      ],
      "text/plain": [
       "09:14:00.535 | \u001b[36mINFO\u001b[0m    | Flow run\u001b[35m 'silver-uakari'\u001b[0m - Finished in state \u001b[32mCompleted\u001b[0m()\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "from prefect import flow, task, get_run_logger\n",
    "import pandas as pd\n",
    "from sqlalchemy import create_engine, text\n",
    "import pymysql  # required by mysql+pymysql\n",
    "import os\n",
    "\n",
    "# -----------------------------\n",
    "# DB CONFIG\n",
    "# -----------------------------\n",
    "DB_USER = \"root\"\n",
    "DB_PASSWORD = \"Oman99690050#\"   # your real password\n",
    "DB_HOST = \"localhost\"\n",
    "DB_NAME = \"pythonDB\"\n",
    "\n",
    "DB_URL = f\"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:3306/{DB_NAME}\"\n",
    "\n",
    "\n",
    "# -----------------------------\n",
    "# 1) EXTRACT (CSV -> DataFrame)\n",
    "# -----------------------------\n",
    "@task\n",
    "def extract_train() -> pd.DataFrame:\n",
    "    logger = get_run_logger()\n",
    "    file_path = \"train.csv\"\n",
    "\n",
    "    if not os.path.exists(file_path):\n",
    "        raise FileNotFoundError(\"train.csv not found in current directory!\")\n",
    "\n",
    "    df = pd.read_csv(file_path)\n",
    "    logger.info(f\"Extracted {len(df)} rows from train.csv\")\n",
    "    return df\n",
    "\n",
    "\n",
    "# -----------------------------\n",
    "# 2) LOAD (DataFrame -> raw table)\n",
    "# -----------------------------\n",
    "@task\n",
    "def load_raw(df: pd.DataFrame):\n",
    "    logger = get_run_logger()\n",
    "    engine = create_engine(DB_URL)\n",
    "    # store raw Titanic data\n",
    "    df.to_sql(\"titanic_raw\", engine, if_exists=\"replace\", index=False)\n",
    "    logger.info(\"Loaded raw data into table 'titanic_raw'\")\n",
    "\n",
    "\n",
    "# -----------------------------\n",
    "# 3) TRANSFORM (INSIDE MySQL)\n",
    "# -----------------------------\n",
    "@task\n",
    "def transform_in_db():\n",
    "    logger = get_run_logger()\n",
    "    engine = create_engine(DB_URL)\n",
    "\n",
    "    with engine.begin() as conn:\n",
    "        # 3.1 Create clean table\n",
    "        conn.execute(text(\"\"\"\n",
    "        DROP TABLE IF EXISTS titanic_clean\n",
    "        \"\"\"))\n",
    "\n",
    "        conn.execute(text(\"\"\"\n",
    "        CREATE TABLE IF NOT EXISTS titanic_clean (\n",
    "            PassengerId INT,\n",
    "            Survived TINYINT,\n",
    "            Pclass TINYINT,\n",
    "            Name VARCHAR(200),\n",
    "            Sex VARCHAR(10),\n",
    "            Age FLOAT,\n",
    "            SibSp INT,\n",
    "            Parch INT,\n",
    "            Ticket VARCHAR(50),\n",
    "            Fare FLOAT,\n",
    "            Cabin VARCHAR(50),\n",
    "            Embarked VARCHAR(5)\n",
    "        )\n",
    "        \"\"\"))\n",
    "\n",
    "        # 3.2 Insert cleaned data from raw\n",
    "        # Simple example: keep subset and drop rows with NULL Age or Fare\n",
    "        conn.execute(text(\"\"\"\n",
    "        INSERT INTO titanic_clean\n",
    "            (PassengerId, Survived, Pclass, Name, Sex,\n",
    "             Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked)\n",
    "        SELECT\n",
    "            PassengerId,\n",
    "            Survived,\n",
    "            Pclass,\n",
    "            Name,\n",
    "            Sex,\n",
    "            Age,\n",
    "            SibSp,\n",
    "            Parch,\n",
    "            Ticket,\n",
    "            Fare,\n",
    "            Cabin,\n",
    "            Embarked\n",
    "        FROM titanic_raw\n",
    "        WHERE Age IS NOT NULL\n",
    "          AND Fare IS NOT NULL\n",
    "        \"\"\"))\n",
    "\n",
    "    logger.info(\"Transform step completed inside MySQL (titanic_clean filled)\")\n",
    "\n",
    "\n",
    "# -----------------------------\n",
    "# 4) ELT FLOW\n",
    "# -----------------------------\n",
    "@flow\n",
    "def elt_titanic_flow():\n",
    "    df = extract_train()   # E\n",
    "    load_raw(df)           # L\n",
    "    transform_in_db()      # T\n",
    "\n",
    "\n",
    "# Run the flow in Jupyter\n",
    "elt_titanic_flow()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "97a07184-79de-42be-ab43-2973ec74b95b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">09:14:05.587 | <span style=\"color: #008080; text-decoration-color: #008080\">INFO</span>    | Flow run<span style=\"color: #800080; text-decoration-color: #800080\"> 'passionate-bonobo'</span> - Beginning flow run<span style=\"color: #800080; text-decoration-color: #800080\"> 'passionate-bonobo'</span> for flow<span style=\"color: #800080; text-decoration-color: #800080; font-weight: bold\"> 'elt-titanic-flow'</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "09:14:05.587 | \u001b[36mINFO\u001b[0m    | Flow run\u001b[35m 'passionate-bonobo'\u001b[0m - Beginning flow run\u001b[35m 'passionate-bonobo'\u001b[0m for flow\u001b[1;35m 'elt-titanic-flow'\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">09:14:05.593 | <span style=\"color: #008080; text-decoration-color: #008080\">INFO</span>    | Flow run<span style=\"color: #800080; text-decoration-color: #800080\"> 'passionate-bonobo'</span> - View at <span style=\"color: #0000ff; text-decoration-color: #0000ff\">https://app.prefect.cloud/account/5a41b131-4cbc-419c-9685-bef0b843bc45/workspace/e31d45fa-dde7-4d90-9e9c-6489ae12e97f/runs/flow-run/06922981-ce00-7fd9-8000-9f591349ee28</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "09:14:05.593 | \u001b[36mINFO\u001b[0m    | Flow run\u001b[35m 'passionate-bonobo'\u001b[0m - View at \u001b[94mhttps://app.prefect.cloud/account/5a41b131-4cbc-419c-9685-bef0b843bc45/workspace/e31d45fa-dde7-4d90-9e9c-6489ae12e97f/runs/flow-run/06922981-ce00-7fd9-8000-9f591349ee28\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">09:14:06.398 | <span style=\"color: #008080; text-decoration-color: #008080\">INFO</span>    | Task run 'extract_train-48b' - Extracted 891 rows from train.csv\n",
       "</pre>\n"
      ],
      "text/plain": [
       "09:14:06.398 | \u001b[36mINFO\u001b[0m    | Task run 'extract_train-48b' - Extracted 891 rows from train.csv\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">09:14:06.409 | <span style=\"color: #008080; text-decoration-color: #008080\">INFO</span>    | Task run 'extract_train-48b' - Finished in state <span style=\"color: #008000; text-decoration-color: #008000\">Completed</span>()\n",
       "</pre>\n"
      ],
      "text/plain": [
       "09:14:06.409 | \u001b[36mINFO\u001b[0m    | Task run 'extract_train-48b' - Finished in state \u001b[32mCompleted\u001b[0m()\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">09:14:07.425 | <span style=\"color: #008080; text-decoration-color: #008080\">INFO</span>    | Task run 'load_raw-224' - Loaded raw data into table 'titanic_raw'\n",
       "</pre>\n"
      ],
      "text/plain": [
       "09:14:07.425 | \u001b[36mINFO\u001b[0m    | Task run 'load_raw-224' - Loaded raw data into table 'titanic_raw'\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">09:14:07.441 | <span style=\"color: #008080; text-decoration-color: #008080\">INFO</span>    | Task run 'load_raw-224' - Finished in state <span style=\"color: #008000; text-decoration-color: #008000\">Completed</span>()\n",
       "</pre>\n"
      ],
      "text/plain": [
       "09:14:07.441 | \u001b[36mINFO\u001b[0m    | Task run 'load_raw-224' - Finished in state \u001b[32mCompleted\u001b[0m()\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">09:14:08.333 | <span style=\"color: #008080; text-decoration-color: #008080\">INFO</span>    | Task run 'transform_in_db-5af' - Transform step completed inside MySQL (titanic_clean filled)\n",
       "</pre>\n"
      ],
      "text/plain": [
       "09:14:08.333 | \u001b[36mINFO\u001b[0m    | Task run 'transform_in_db-5af' - Transform step completed inside MySQL (titanic_clean filled)\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">09:14:08.345 | <span style=\"color: #008080; text-decoration-color: #008080\">INFO</span>    | Task run 'transform_in_db-5af' - Finished in state <span style=\"color: #008000; text-decoration-color: #008000\">Completed</span>()\n",
       "</pre>\n"
      ],
      "text/plain": [
       "09:14:08.345 | \u001b[36mINFO\u001b[0m    | Task run 'transform_in_db-5af' - Finished in state \u001b[32mCompleted\u001b[0m()\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">09:14:08.735 | <span style=\"color: #008080; text-decoration-color: #008080\">INFO</span>    | Flow run<span style=\"color: #800080; text-decoration-color: #800080\"> 'passionate-bonobo'</span> - Finished in state <span style=\"color: #008000; text-decoration-color: #008000\">Completed</span>()\n",
       "</pre>\n"
      ],
      "text/plain": [
       "09:14:08.735 | \u001b[36mINFO\u001b[0m    | Flow run\u001b[35m 'passionate-bonobo'\u001b[0m - Finished in state \u001b[32mCompleted\u001b[0m()\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "elt_titanic_flow()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cce65584-1653-4dab-8aee-0d8d9945e815",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python (prefect_env)",
   "language": "python",
   "name": "prefect_env"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
