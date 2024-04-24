import pandas as pd

from llama_index.schema import Document


class DataLoader():

    _dataset_name = './data/imdb_top_1000.csv'
    _dataframe = None
    _concatenated_column_name = 'concatenated'
    _documents = []

    def __init__(self):
        self._dataframe = pd.read_csv(self._dataset_name)
        self.__add_concatenated_column()
        self._dataframe.apply(lambda row: self._documents.append(
                Document(text=row[self._concatenated_column_name])),
            axis=1)

    def __add_concatenated_column(self):
        self._dataframe[self._concatenated_column_name] = self._dataframe.apply(
            lambda row: '\n'.join(
                [
                    f"Title: {str(row['Series_Title'])}",
                    f"Overview: {str(row['Overview'])}",
                    f"Released year: {str(row['Released_Year'])}",
                    f"Runtime: {str(row['Runtime'])}",
                    f"Genre: {str(row['Genre'])}",
                    f"IMDB Rating: {str(row['IMDB_Rating'])}",
                    f"Meta Score: {str(row['Meta_score'])}",
                    f"Number of Votes: {str(row['No_of_Votes'])}",
                    f"Gross sales: {str(row['Gross'])}",
                    f"Director: {str(row['Director'])}",
                    f"Stars: {str(row['Star1'])}, {str(row['Star2'])}, {str(row['Star3'])}, {str(row['Star4'])}",
                    f"Director: {str(row['Director'])}"
                ]),
            axis=1)

    @property
    def documents(self):
        return self._documents
