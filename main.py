from bigmac_stats import BigMacStats

def main():
    try:
        shapefile_path = "ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp"
        
        analyzer = BigMacStats(
            file_path='BigmacPrice.csv',
            shapefile_path=shapefile_path
        )
        
        analyzer.show_world_map()
        analyzer.show_histogram()
    
    except Exception as e:
        print(f"Ошибка: {str(e)}")
        print("Инструкция по установке:")
        print("1. Скачайте данные с https://www.naturalearthdata.com/downloads/110m-cultural-vectors/")
        print("2. Распакуйте архив в папку с проектом")

if __name__ == "__main__":
    main()