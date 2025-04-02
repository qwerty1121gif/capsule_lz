from bigmac_stats import BigMacStats

def main():
    try:
        analyzer = BigMacStats('BigmacPrice.csv')
        
        # Основные функции
        analyzer.show_table()
        analyzer.show_histogram()
        
        # Дополнительная функция
        analyzer.show_heatmap()
        
    except FileNotFoundError:
        print("Ошибка: Файл BigmacPrice.csv не найден!")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

if __name__ == "__main__":
    main()