<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_2.fl"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 07:31:47 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDY6Mzk6NTUgUE07MjU4OQ=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDc6MzE6NDcgUE07MjsyNjky"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <declare name="coffeeQty, teaQty, total, quantity, menu" type="Integer" array="False" size=""/>
            <declare name="coffeePrice, teaPrice" type="Integer" array="False" size=""/>
            <assign variable="coffeePrice" expression="25"/>
            <assign variable="teaPrice" expression="20"/>
            <assign variable="coffeeQty" expression="10"/>
            <assign variable="teaQty" expression="0"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea): &quot;" newline="True"/>
            <input variable="menu"/>
            <if expression="menu==1">
                <then>
                    <output expression="&quot;Enter quantity: &quot;" newline="True"/>
                    <input variable="quantity"/>
                    <if expression="quantity&lt;=10">
                        <then>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <assign variable="total" expression="quantity * coffeePrice"/>
                            <output expression="&quot;Total Price : &quot; &amp; total &amp; &quot; Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <output expression="&quot;Enter quantity: &quot;" newline="True"/>
                    <input variable="quantity"/>
                    <if expression="quantity==0">
                        <then>
                            <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                            <assign variable="total" expression="quantity * teaPrice"/>
                            <output expression="&quot;Total Price : &quot; &amp; total &amp; &quot; Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>