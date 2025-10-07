<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_2"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-22 08:49:04 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDY6MTE6MzkgUE07MjU4MQ=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDY6MzU6MTggUE07MTsyNjky"/>
        <attribute name="edited" value="ZWxheHk7Q0hBTk9OQ0hPVEk7MjAyNS0wNy0yMjswODo0MTo0OSBQTTsxO2NvbXB1dGVyO0NQQ09NOzI1NjgtMDctMTc7MDM6NTU6MTQgUE07cmFiYml0XzY4MzM4MDY5NF82LmZwcmc7NzI1Mg=="/>
        <attribute name="edited" value="ZWxheHk7Q0hBTk9OQ0hPVEk7MjAyNS0wNy0yMjswODo0OTowNCBQTTs0OzI3NjE="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="coffeePrice, coffeeQty" type="Real" array="False" size=""/>
            <declare name="menu" type="Integer" array="False" size=""/>
            <output expression="&quot;Beverage List: &quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea): &quot;" newline="True"/>
            <assign variable="coffeePrice" expression="25"/>
            <declare name="Select, Qty, price" type="Integer" array="False" size=""/>
            <input variable="select"/>
            <output expression="&quot;Enter quantity: &quot;" newline="True"/>
            <input variable="Qty"/>
            <if expression="select = 1">
                <then>
                    <if expression="Qty = 10">
                        <then>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <assign variable="price" expression="coffeePrice*qty"/>
                            <output expression="&quot;Total Price : &quot;&amp;price&amp; &quot;Baht&quot;" newline="True"/>
                        </else>
                    </if>
                    <output expression="&quot;Enjoy!&quot;" newline="True"/>
                </then>
                <else>
                    <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>