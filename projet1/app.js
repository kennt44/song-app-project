// state
let currCity = "London"; // Variable to store the current city, initialized with "London"
let units = "metric"; // Variable to store the units for temperature, initialized with "metric"

// Selectors
let city = document.querySelector(".weather__city"); // Selecting the element with class "weather__city"
let datetime = document.querySelector(".weather__datetime"); // Selecting the element with class "weather__datetime"
let weather__forecast = document.querySelector('.weather__forecast'); // Selecting the element with class "weather__forecast"
let weather__temperature = document.querySelector(".weather__temperature"); // Selecting the element with class "weather__temperature"
let weather__icon = document.querySelector(".weather__icon"); // Selecting the element with class "weather__icon"
let weather__minmax = document.querySelector(".weather__minmax"); // Selecting the element with class "weather__minmax"
let weather__realfeel = document.querySelector('.weather__realfeel'); // Selecting the element with class "weather__realfeel"
let weather__humidity = document.querySelector('.weather__humidity'); // Selecting the element with class "weather__humidity"
let weather__wind = document.querySelector('.weather__wind'); // Selecting the element with class "weather__wind"
let weather__pressure = document.querySelector('.weather__pressure'); // Selecting the element with class "weather__pressure"

// search
document.querySelector(".weather__search").addEventListener('submit', e => {
    let search = document.querySelector(".weather__searchform"); // Selecting the search input field
    // prevent default action
    e.preventDefault(); // Preventing the default form submission behavior
    // change current city
    currCity = search.value; // Updating the current city with the value from the search input field
    // get weather forecast 
    getWeather(); // Calling the getWeather function to fetch weather data for the new city
    // clear form
    search.value = ""; // Clearing the search input field
})

// units
document.querySelector(".weather_unit_celsius").addEventListener('click', () => {
    if(units !== "metric"){
        // change to metric
        units = "metric"; // Setting units to metric
        // get weather forecast 
        getWeather(); // Calling the getWeather function to fetch weather data with metric units
    }
})

document.querySelector(".weather_unit_farenheit").addEventListener('click', () => {
    if(units !== "imperial"){
        // change to imperial
        units = "imperial"; // Setting units to imperial
        // get weather forecast 
        getWeather(); // Calling the getWeather function to fetch weather data with imperial units
    }
})

function convertTimeStamp(timestamp, timezone){
     const convertTimezone = timezone / 3600; // convert seconds to hours 

    const date = new Date(timestamp * 1000); // Converting the timestamp to date object
    
    const options = {
        weekday: "long",
        day: "numeric",
        month: "long",
        year: "numeric",
        hour: "numeric",
        minute: "numeric",
        timeZone: `Etc/GMT${convertTimezone >= 0 ? "-" : "+"}${Math.abs(convertTimezone)}`, // Calculating timezone offset
        hour12: true,
    }
    return date.toLocaleString("en-US", options); // Returning formatted date string
}

// convert country code to name
function convertCountryCode(country){
    let regionNames = new Intl.DisplayNames(["en"], {type: "region"}); // Creating Intl.DisplayNames object
    return regionNames.of(country); // Returning country name
}

function getWeather(){
    const API_KEY = '64f60853740a1ee3ba20d0fb595c97d5'; // API key for OpenWeatherMap

fetch(`https://api.openweathermap.org/data/2.5/weather?q=${currCity}&appid=${API_KEY}&units=${units}`).then(res => res.json()).then(data => {
    console.log(data); // Logging the fetched data
    city.innerHTML = `${data.name}, ${convertCountryCode(data.sys.country)}`; // Setting city name
    datetime.innerHTML = convertTimeStamp(data.dt, data.timezone); // Setting date and time
    weather__forecast.innerHTML = `<p>${data.weather[0].main}`; // Setting weather forecast
    weather__temperature.innerHTML = `${data.main.temp.toFixed()}&#176`; // Setting temperature
    weather__icon.innerHTML = `   <img src="http://openweathermap.org/img/wn/${data.weather[0].icon}@4x.png" />`; // Setting weather icon
    weather__minmax.innerHTML = `<p>Min: ${data.main.temp_min.toFixed()}&#176</p><p>Max: ${data.main.temp_max.toFixed()}&#176</p>`; // Setting min and max temperature
    weather__realfeel.innerHTML = `${data.main.feels_like.toFixed()}&#176`; // Setting real feel temperature
    weather__humidity.innerHTML = `${data.main.humidity}%`; // Setting humidity
    weather__wind.innerHTML = `${data.wind.speed} ${units === "imperial" ? "mph": "m/s"}`; // Setting wind speed
    weather__pressure.innerHTML = `${data.main.pressure} hPa`; // Setting pressure
})
}

document.body.addEventListener('load', getWeather()); // When the body is loaded, fetch weather data
