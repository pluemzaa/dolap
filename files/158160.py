<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="683380460-1_1"/>
        <attribute name="authors" value="acer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-21 01:51:43 PM"/>
        <attribute name="created" value="YWNlcjtMQVBUT1AtNzFQQ09EM0w7MjU2OC0wNy0xOTswMzoyNjoyNCBQTTsyNzQ0"/>
        <attribute name="edited" value="YWNlcjtMQVBUT1AtNzFQQ09EM0w7MjU2OC0wNy0yMTswMTo1MTo0MyBQTTsyOzI4NDM="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="menu" type="Integer" array="False" size=""/>
            <declare name="quantity, coffeeQty, teaQty, coffeePrice, teaPrice, total" type="Integer" array="False" size=""/>
            <assign variable="coffeePrice" expression="25"/>
            <assign variable="teaPrice" expression="20"/>
            <assign variable="coffeeQty" expression="10"/>
            <assign variable="teaQty" expression="0"/>
            <assign variable="total" expression="0"/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea): &quot;" newline="True"/>
            <input variable="menu"/>
            <output expression="&quot;Enter quantity: &quot;" newline="True"/>
            <input variable="quantity"/>
            <if expression="(menu = 1 AND quantity &gt; coffeeQty) OR (menu = 2 AND quantity &gt; teaQty)">
                <then>
                    <if expression="menu = 1">
                        <then>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <if expression="menu = 1">
                        <then>
                            <assign variable="total" expression="quantity * coffeePrice"/>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <output expression="&quot;Total Price : &quot; &amp; total &amp; &quot; Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <assign variable="total" expression="quantity * teaPrice"/>
                            <output expression="&quot;You purchased Tea&quot;" newline="True"/>
                            <output expression="&quot;Total Price : &quot; &amp; total &amp; &quot; Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </else>
                    </if>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>