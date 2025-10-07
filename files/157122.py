<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="Flow125-5 .2"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 05:04:40 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDQ6MzM6NDEgUE07MjU3Ng=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDU6MDQ6NDAgUE07MTsyNjgy"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="menu, coffeePrice, coffeeQty, total" type="Integer" array="False" size=""/>
            <assign variable="coffeePrice" expression="25"/>
            <assign variable="coffeeQty" expression="10"/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea): &quot;" newline="True"/>
            <input variable="menu"/>
            <output expression="&quot;Enter quantity: &quot;" newline="True"/>
            <input variable="coffeeQty"/>
            <assign variable="total" expression="coffeeQty*coffeePrice"/>
            <if expression="menu==1">
                <then>
                    <if expression="coffeeQty&lt;=10">
                        <then>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <output expression="&quot;Total Price : &quot;&amp; total &amp;&quot; Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>