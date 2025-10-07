<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="rrq"/>
        <attribute name="authors" value="Anurak"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-20 03:31:45 PM"/>
        <attribute name="created" value="QW51cmFrO05BWTsyNTY4LTA3LTIwOzAyOjU1OjU4IFBNOzIxNDE="/>
        <attribute name="edited" value="QW51cmFrO05BWTsyNTY4LTA3LTIwOzAzOjMxOjQ1IFBNOzI7MjI0MQ=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="menu, coffeePrice, coffeeQty, teaPrice, teaQty, orderQty, totalPrice" type="Integer" array="False" size=""/>
            <assign variable="coffeePrice" expression="25"/>
            <assign variable="coffeeQty" expression="10"/>
            <assign variable="teaPrice" expression="20"/>
            <assign variable="teaQty" expression="0"/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea):  &quot;" newline="True"/>
            <input variable="menu"/>
            <output expression="&quot;Enter quantity:&quot;" newline="True"/>
            <input variable="orderQty"/>
            <if expression="menu==1">
                <then>
                    <if expression="orderQty &gt; coffeeQty">
                        <then>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </then>
                        <else>
                            <assign variable="totalPrice" expression="orderQty * coffeePrice"/>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <output expression="&quot;Total Price : &quot; &amp; totalPrice &amp; &quot; Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <if expression="menu==2">
                        <then>
                            <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
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