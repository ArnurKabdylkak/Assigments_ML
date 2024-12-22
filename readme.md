# Assignment 1 by Kabdylkak Arnur Nurlanuly

## RU

### Шаг 1: Сбор данных
Я собрал данные, объединив несколько JSON-файлов из папки `D:/ShoppingAppReviews Dataset/ShoppingAppReviews/json`. Каждый файл представлял данные с различных торговых платформ, таких как Amazon, Walmart и других. Все записи были объединены в единый DataFrame для анализа.

### Шаг 2: Исследовательский анализ данных (EDA)
Я провёл анализ данных и создал следующие визуализации:
1. **Распределение рейтингов**:
   - Построил гистограмму, чтобы изучить распределение рейтингов между платформами.
   - Сохранил график как `ratings_distribution.png`.

2. **Количество отзывов по платформам**:
   - Построил столбчатую диаграмму, отображающую количество отзывов для каждой платформы.
   - Сохранил график как `reviews_by_platform.png`.

3. **Рейтинги по категориям**:
   - Построил боксплот, чтобы визуализировать, как варьируются рейтинги между категориями, такими как Electronics, Fashion и Groceries.
   - Сохранил график как `ratings_by_category.png`.

### Шаг 3: Обработка пропущенных значений
Я проверил наличие пропущенных значений (NaN) в данных. К счастью, пропущенных значений не обнаружено, поэтому дополнительные действия не потребовались.

### Шаг 4: Определение числовых и категориальных столбцов
Я классифицировал столбцы на:
- **Числовые столбцы**: Включают `Reviews` и `Ratings`.
- **Категориальные столбцы**: Включают `Platform` и `Category`.

### Шаг 5: Кодирование категориальных данных
Я закодировал категориальные столбцы двумя способами:
1. **One-Hot Encoding**: Преобразовал категориальные переменные в бинарные столбцы.
2. **Label Encoding**: Присвоил числовые метки каждой категории.

Эти методы обеспечили готовность данных для использования в моделях машинного обучения.

### Шаг 6: Анализ корреляций
Я вычислил коэффициенты корреляции между числовыми столбцами (`Reviews` и `Ratings`), чтобы выявить значимые взаимосвязи. Дополнительно:
- Создал тепловую карту корреляций для визуализации этих взаимосвязей.
- Сохранил график как `correlation_matrix.png`.

### Шаг 7: Подготовка отчёта
Наконец, я обработал и сохранил итоговый набор данных в файл `processed_shopping_data.csv`. Все графики были задокументированы и включены в задание.

---

## EN

### Step 1: Data Collection
I collected the dataset by consolidating multiple JSON files from the folder `D:/ShoppingAppReviews Dataset/ShoppingAppReviews/json`. Each file represented data from different shopping platforms like Amazon, Walmart, and others. I combined all records into a single DataFrame for analysis.

### Step 2: Exploratory Data Analysis (EDA)
I analyzed the dataset by creating the following visualizations:
1. **Ratings Distribution**:
   - Created a histogram to observe the distribution of ratings across platforms.
   - Saved the visualization as `ratings_distribution.png`.

2. **Reviews by Platform**:
   - Generated a bar chart showing the number of reviews for each platform.
   - Saved the visualization as `reviews_by_platform.png`.

3. **Ratings by Category**:
   - Used a box plot to visualize how ratings varied across different categories like Electronics, Fashion, and Groceries.
   - Saved the visualization as `ratings_by_category.png`.

### Step 3: Handling Missing Values
I checked the dataset for any missing values (NaN). Fortunately, no missing values were found, so no additional imputation was required.

### Step 4: Identifying Numeric and Categorical Columns
I classified the columns into:
- **Numeric Columns**: Includes `Reviews` and `Ratings`.
- **Categorical Columns**: Includes `Platform` and `Category`.

### Step 5: Encoding Categorical Data
I encoded the categorical columns using two methods:
1. **One-Hot Encoding**: Transformed categorical variables into binary columns.
2. **Label Encoding**: Assigned numerical labels to each category.

These techniques ensured the data was ready for machine learning models.

### Step 6: Correlation Analysis
I calculated the correlation coefficients between numeric columns (`Reviews` and `Ratings`) to identify any significant relationships. Additionally:
- Created a correlation matrix heatmap to visualize these relationships.
- Saved the visualization as `correlation_matrix.png`.

### Step 7: Report Preparation
Finally, I processed and saved the final dataset to `processed_shopping_data.csv`. All visualizations were documented and included in this assignment.

---

