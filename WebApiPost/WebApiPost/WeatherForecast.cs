namespace WebApiPost
{
    /// <summary>
    /// Цей клас кланий козак
    /// </summary>
    public class WeatherForecast
    {
        /// <summary>
        /// Дата прогнозу погоди
        /// </summary>
        public DateOnly Date { get; set; }

        /// <summary>
        /// Температура в градусах Цельсія
        /// </summary>
        public int TemperatureC { get; set; }

        /// <summary>
        /// Температура в градусах Фаренгейта, обчислюється на основі TemperatureC
        /// </summary>
        public int TemperatureF => 32 + (int)(TemperatureC / 0.5556);

        /// <summary>
        /// Представлення погоди у вигляді тексту (наприклад, "Сонячно", "Дощ", "Хмарно")
        /// </summary>
        public string? Summary { get; set; }
    }
}
