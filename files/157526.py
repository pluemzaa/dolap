<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="Flowchart.lap2"/>
        <attribute name="authors" value="User"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-21 02:41:50 PM"/>
        <attribute name="created" value="VXNlcjtMQVBUT1AtQVNBRkZPNlY7MjAyNS0wNy0yMTswMjoyNjozMSBQTTsyNzcz"/>
        <attribute name="edited" value="VXNlcjtMQVBUT1AtQVNBRkZPNlY7MjAyNS0wNy0yMTswMjo0MTo1MCBQTTsxOzI4Nzk="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="menu, coffeePrice, coffeeQty, teaPrice, teaQty, quantity, total" type="Integer" array="False" size=""/>
            <assign variable="coffeePrice" expression="25"/>
            <assign variable="coffeeQty" expression="10"/>
            <assign variable="teaPrice" expression="20"/>
            <assign variable="teaQty" expression="0"/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea):&quot;" newline="True"/>
            <input variable="menu"/>
            <output expression="&quot;Enter quantity:&quot;" newline="True"/>
            <input variable="quantity"/>
            <if expression="menu==1">
                <then>
                    <if expression="quantity&lt;=10">
                        <then>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <assign variable="total" expression="coffeePrice*quantity"/>
                            <output expression="&quot;Total Price :&quot; &amp; total &amp; &quot; Baht &quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <if expression="quantity==0">
                        <then>
                            <output expression="&quot;You purchased Tea&quot;" newline="True"/>
                            <assign variable="total" expression="teaPrice*quantity"/>
                            <output expression="&quot;Total Price :&quot; &amp; total &amp; &quot; Baht &quot;" newline="True"/>
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