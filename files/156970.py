<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_test-2"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 03:05:59 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDI6MzY6MTUgUE07MjU3OA=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDM6MDU6NTkgUE07MjsyNjky"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="menu, quantity, coffeeprice, teaprice, total, coffeeqty, teaqty" type="Integer" array="False" size=""/>
            <assign variable="coffeeprice" expression="25"/>
            <assign variable="teaprice" expression="20"/>
            <assign variable="coffeeqty" expression="10"/>
            <assign variable="teaqty" expression="0"/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea): &quot;" newline="True"/>
            <input variable="menu"/>
            <if expression="menu==1">
                <then>
                    <output expression="&quot;Enter quantity: &quot;" newline="True"/>
                    <input variable="quantity"/>
                    <if expression="quantity&gt;coffeeqty">
                        <then>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <assign variable="total" expression="coffeeprice*quantity"/>
                            <output expression="&quot;Total Price : &quot; &amp; total &amp; &quot; Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <if expression="menu==2">
                        <then>
                            <output expression="&quot;Enter quantity: &quot;" newline="True"/>
                            <input variable="quantity"/>
                            <if expression="quantity&gt;=teaqty">
                                <then>
                                    <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                                </then>
                                <else>
                                    <output expression="&quot;You purchased Tea&quot;" newline="True"/>
                                    <assign variable="total" expression="teaprice*quantity"/>
                                    <output expression="&quot;Total Price : &quot; &amp; total &amp; &quot; Baht&quot;" newline="True"/>
                                    <output expression="&quot;Enjoy!&quot;" newline="True"/>
                                </else>
                            </if>
                        </then>
                        <else/>
                    </if>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>