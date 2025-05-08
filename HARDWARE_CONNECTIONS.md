
# Hardware Connections Guide

This document provides detailed wiring instructions for connecting all sensors in the sensor-test project to a Raspberry Pi.

## Table of Contents
- [General GPIO Information](#general-gpio-information)
- [MCP3008 ADC Setup](#mcp3008-adc-setup)
- [Digital Sensors](#digital-sensors)
  - [DHT22 Temperature/Humidity Sensor](#dht22-temperaturehumidity-sensor)
  - [Rain Sensor (Digital)](#rain-sensor-digital)
  - [LDR Light Sensor (Digital)](#ldr-light-sensor-digital)
  - [Relay Module (with 2N2222A Transistor)](#relay-module-with-2n2222a-transistor)
- [I2C Sensors](#i2c-sensors)
  - [BMP180 Pressure Sensor](#bmp180-pressure-sensor)
- [Analog Sensors via MCP3008](#analog-sensors-via-mcp3008)
  - [Soil Moisture Sensor](#soil-moisture-sensor)
  - [Rain Sensor (Analog)](#rain-sensor-analog)
  - [LDR Light Sensor (Analog)](#ldr-light-sensor-analog)
- [LCD Display](#lcd-display)
- [LED Connections](#led-connections)

## General GPIO Information

The Raspberry Pi uses BCM (Broadcom) pin numbering in all scripts. This refers to the GPIO numbers, not the physical pin positions on the board.

## MCP3008 ADC Setup

The MCP3008 is an analog-to-digital converter that allows the Raspberry Pi to read analog sensors. It communicates with the Pi using the SPI protocol.

### MCP3008 Pinout
| MCP3008 Pin | Raspberry Pi Connection |
|-------------|-------------------------|
| VDD         | 3.3V                    |
| VREF        | 3.3V                    |
| AGND        | GND                     |
| CLK         | SCLK (GPIO 11)          |
| DOUT        | MISO (GPIO 9)           |
| DIN         | MOSI (GPIO 10)          |
| CS          | CE0 (GPIO 8)            |
| DGND        | GND                     |

### Channel Assignments
The MCP3008 has 8 analog input channels (0-7):
- Channel 0: Soil Moisture Sensor
- Channel 1: LDR Light Sensor (Analog)
- Channel 2: Rain Sensor (Analog)

## Digital Sensors

### DHT22 Temperature/Humidity Sensor

| DHT22 Pin | Raspberry Pi Connection | Notes                      |
|-----------|-------------------------|----------------------------|
| VCC       | 3.3V                    | Some DHT22 modules work with 5V |
| DATA      | GPIO 26                 | Connect a 4.7kΩ-10kΩ pull-up resistor between DATA and VCC |
| GND       | GND                     |                            |

### Rain Sensor (Digital)

| Rain Sensor Pin | Raspberry Pi Connection | Notes                      |
|-----------------|-------------------------|----------------------------|
| VCC             | 3.3V or 5V             | Check your module's voltage requirements |
| GND             | GND                     |                            |
| DO (Digital Out)| GPIO 17                 | Digital output (HIGH/LOW)  |

### LDR Light Sensor (Digital)

| LDR Sensor Pin | Raspberry Pi Connection | Notes                      |
|----------------|-------------------------|----------------------------|
| VCC            | 3.3V or 5V             | Check your module's voltage requirements |
| GND            | GND                     |                            |
| DO (Digital Out)| GPIO 4                 | Digital output (HIGH/LOW)  |

### Relay Module (with 2N2222A Transistor)

| Relay Pin      | Connection                | Notes                      |
|----------------|---------------------------|----------------------------|
| VCC            | 5V                        | Most relay modules require 5V |
| GND            | GND                       |                            |
| IN (Signal)    | Collector of 2N2222A      | Controlled by transistor   |

#### 2N2222A Transistor Connections

| Transistor Pin | Connection                | Notes                      |
|----------------|---------------------------|----------------------------|
| Base           | GPIO 21 via 1kΩ resistor  | Connect a 1kΩ resistor between GPIO and transistor base |
| Emitter        | GND                       | Connected to ground        |
| Collector      | Relay IN                  | Connected to relay input signal pin |

## I2C Sensors

### BMP180 Pressure Sensor

The BMP180 uses I2C communication protocol.

| BMP180 Pin | Raspberry Pi Connection | Notes                      |
|------------|-------------------------|----------------------------|
| VCC        | 3.3V                    | Do not connect to 5V       |
| GND        | GND                     |                            |
| SCL        | GPIO 3 (SCL)            | I2C clock line             |
| SDA        | GPIO 2 (SDA)            | I2C data line              |

## Analog Sensors via MCP3008

### Soil Moisture Sensor

| Soil Moisture Pin | Connection                | Notes                      |
|-------------------|---------------------------|----------------------------|
| VCC               | 3.3V or 5V               | Check your module's voltage requirements |
| GND               | GND                       |                            |
| AO (Analog Out)   | MCP3008 Channel 0         | Analog output (0-1023)     |

### Rain Sensor (Analog)

| Rain Sensor Pin   | Connection                | Notes                      |
|-------------------|---------------------------|----------------------------|
| VCC               | 3.3V or 5V               | Check your module's voltage requirements |
| GND               | GND                       |                            |
| AO (Analog Out)   | MCP3008 Channel 2         | Analog output (0-1023)     |

### LDR Light Sensor (Analog)

| LDR Sensor Pin    | Connection                | Notes                      |
|-------------------|---------------------------|----------------------------|
| VCC               | 3.3V or 5V               | Check your module's voltage requirements |
| GND               | GND                       |                            |
| AO (Analog Out)   | MCP3008 Channel 1         | Analog output (0-1023)     |

## LCD Display

The 16x2 LCD display is connected using GPIO pins in 4-bit mode.

| LCD Pin | Raspberry Pi Connection | Notes                      |
|---------|-------------------------|----------------------------|
| VSS     | GND                     | Power ground               |
| VDD     | 5V                      | Power positive             |
| V0      | GND via potentiometer   | Connect a 5kΩ resistor or 10kΩ potentiometer between V0 and GND for contrast adjustment |
| RS      | GPIO 25                 | Register Select            |
| RW      | GND                     | Read/Write (GND for write-only) |
| E       | GPIO 24                 | Enable                     |
| D0-D3   | Not connected           | Not used in 4-bit mode     |
| D4      | GPIO 23                 | Data bit 4                 |
| D5      | GPIO 17                 | Data bit 5                 |
| D6      | GPIO 18                 | Data bit 6                 |
| D7      | GPIO 22                 | Data bit 7                 |
| A       | 3.3V or 5V via resistor | Backlight anode            |
| K       | GND                     | Backlight cathode          |

## LED Connections

For the police lights demo:

| LED      | Raspberry Pi Connection | Notes                      |
|----------|-------------------------|----------------------------|
| Red LED  | GPIO 17                 | Connect with a 220Ω-330Ω resistor |
| Blue LED | GPIO 18                 | Connect with a 220Ω-330Ω resistor |

## Wiring Diagram

```
                       +-------------+
                       | Raspberry Pi|
                       +-------------+
                       |             |
+-------+              |             |              +--------+
| DHT22 |---[DATA]-----|GPIO 26      |              | BMP180 |
+-------+              |             |              +--------+
                       |             |---[SCL]------|SCL     |
+------------+         |             |              |        |
|Rain Sensor |--[DO]---|GPIO 17      |---[SDA]------|SDA     |
|(Digital)   |         |             |              +--------+
+------------+         |             |
                       |             |              +---------+
+-----------+          |             |              |  16x2   |
|LDR Sensor |--[DO]----|GPIO 4       |---[RS]-------|LCD      |
|(Digital)  |          |             |---[E]--------|Display  |
+-----------+          |             |---[D4-D7]----|         |
                       |             |              +---------+
+---------+            |             |
| Relay   |--[IN]------|             |              +---------+
+---------+    |       |             |              |Police   |
               |       |             |---[GPIO 17]--|Lights   |
               |       |             |---[GPIO 18]--|         |
               |       |             |              +---------+
               |       |             |
+-----------+  |       |             |              +---------+
| 2N2222A   |  |       |             |              |         |
| Transistor|<-+       |             |              | MCP3008 |
|           |          |             |---[SCLK]-----|CLK      |
| [Base]<---|---[1kΩ]--|GPIO 21      |---[MISO]-----|DOUT     |
| [Emitter]-|---GND    |             |---[MOSI]-----|DIN      |
| [Collector]--[Relay IN]            |---[CE0]------|CS       |
+-----------+          |             |              |         |
                       +-------------+              +---------+
                                                    |         |
                                                    |CH0      |---[AO]---+------------+
                                                    |         |          |Soil Moisture|
                                                    |CH1      |---[AO]---+------------+
                                                    |         |
                                                    |CH2      |---[AO]---+------------+
                                                    |         |          |Rain Sensor  |
                                                    +---------+          |(Analog)     |
                                                                        +------------+
                                                                        
                                                                        +------------+
                                                                        |LDR Sensor   |
                                                                        |(Analog)     |
                                                                        +------------+
```

## Notes

1. **Power Supply**: Ensure your Raspberry Pi has a stable power supply, especially when connecting multiple sensors.
2. **Voltage Levels**: Most sensors work with 3.3V logic, but some modules may require 5V for power.
3. **Pull-up/Pull-down Resistors**: Some sensors may require external pull-up or pull-down resistors.
4. **MCP3008 Channels**: The channel assignments can be changed in the respective scripts if needed.
5. **Relay Control**: The relay is controlled via a 2N2222A transistor. GPIO 21 connects to the transistor base through a 1kΩ resistor, emitter to GND, collector to relay IN.
6. **LCD Contrast**: Use a 5kΩ resistor or a 10kΩ potentiometer between V0 and GND to adjust LCD contrast.
