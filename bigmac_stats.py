import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class BigMacStats:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
        self.preprocess_data()
        
    def preprocess_data(self):
        # Преобразование даты в год
        self.df['year'] = pd.to_datetime(self.df['date']).dt.year
        
        # Создание сводной таблицы для тепловой карты
        self.heatmap_data = self.df.pivot_table(
            index='name',
            columns='year',
            values='dollar_price',
            aggfunc='mean'
        )
        
    def show_heatmap(self):
        plt.figure(figsize=(18, 12))
        
        # Настройка цветовой палитры
        cmap = sns.diverging_palette(220, 20, as_cmap=True)
        
        # Создание тепловой карты
        sns.heatmap(
            self.heatmap_data,
            annot=True,
            fmt=".1f",
            cmap=cmap,
            linewidths=.5,
            cbar_kws={'label': 'Средняя цена в долларах'}
        )
        
        # Настройка отображения
        plt.title('Динамика цен на Биг Мак по странам и годам', pad=20)
        plt.xlabel('Год')
        plt.ylabel('Страна')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()