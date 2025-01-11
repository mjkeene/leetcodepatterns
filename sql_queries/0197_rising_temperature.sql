with ordered_weather_data as (
    select id
    ,recordDate
    ,temperature
    ,lag(temperature) OVER(order by recordDate) as previous_day_temp
    ,lag(recordDate) OVER(order by recordDate) as previous_date
    from Weather
)

select id
from ordered_weather_data
where temperature > previous_day_temp
and recordDate - previous_date = 1