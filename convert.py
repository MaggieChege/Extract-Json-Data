import pandas as pd
import json
from config import SQLALCHEMY_DATABASE_URI

cols_mapper = {'callType': 'calltype',
                       'clientName': 'clientname',
                       'contactType': 'contacttype',
                       'dateCreated': 'datecreated',
                       'dispositionName': 'dispositionname',
                       'mobileNo': 'mobileno',
                       'questionSubType': 'questionsubtype',
                       'questionType': 'questiontype',
                       'sourceName': 'questiontype',
                       'sourceName': 'sourcename',
                       'storeName': 'storename',
                       'ticketID': 'ticketid'}


class ConvertData(object):

    def __init__(self):
        from Model import db
        db.drop_all()
        db.create_all()
        data = pd.read_json('interview_201909.json')
        df = pd.read_json(json.dumps(data[0][1]['Report']))
        self.df = df.rename(columns=cols_mapper)
        self.engine = SQLALCHEMY_DATABASE_URI



    def populate_disposition_table(self):

        new = pd.DataFrame(self.df['dispositionname'].unique())
        newdf = new.rename(columns={0: 'dispositionname'})
        newdf.to_sql(name='disposition', con=self.engine, if_exists='append', index=False)

    def populate_stores_table(self):
        new = pd.DataFrame(self.df['storename'].unique())

        newdf_stores = new.rename(columns={0: 'storename'})
        newdf_stores.to_sql(name='store', con=self.engine, if_exists='append', index=False)


    def get_objects_from_db(self, table_name, column):
        sql = f"SELECT id, {column} FROM {table_name}"
        df = pd.read_sql(sql, con=self.engine)
        #match a value to a key
        items_dict = {}
        for each in range(len(df)):
            each += 1
            items_dict.update(
                {df.iloc[each - 1:each, 1].item(): df.iloc[each - 1:each, 0].item()})
        return items_dict


    def populate_users_data(self):
        # insert normalized data from json file into DB
        self.populate_stores_table()
        self.populate_disposition_table()
        new_data_ = self.df

        new_data_['dispositionname'] = new_data_['dispositionname'].map(
            self.get_objects_from_db('disposition', 'dispositionname'))
        new_data_ = new_data_.rename(columns={'dispositionname': "disposition_id"})
        new_data_['storename'] = new_data_['storename'].map(
            self.get_objects_from_db('store', 'storename'))
        new_data_ = new_data_.rename(columns={'storename': "store_id"})
        new_data_.to_sql(name='users', con=self.engine, if_exists='append', index=False)
