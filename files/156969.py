<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="3281Lab2"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-17 01:49:40 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDI6MjU6MjIgUE07MjU3NA=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDM6MDU6MjUgUE07NTsyNjg4"/>
        <attribute name="edited" value="cHBwcDU7Q0xFTTsyMDI1LTA3LTE3OzAxOjQ5OjQwIFBNOzY7MjE4OQ=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="coffeePrice, coffeeQty, teaPrice, teaQty, menu, quantity, total" type="Integer" array="False" size=""/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea):&quot;" newline="True"/>
            <input variable="menu"/>
            <assign variable="coffeeQty" expression="10"/>
            <assign variable="teaQty" expression="0"/>
            <if expression="menu==1">
                <then>
                    <output expression="&quot;Enter quantity:&quot;" newline="True"/>
                    <input variable="quantity"/>
                    <assign variable="total" expression="quantity * 25"/>
                    <if expression="quantity&lt;=10">
                        <then>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <output expression="&quot;Total Price : &quot; &amp; total" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <if expression="menu==2">
                        <then>
                            <output expression="&quot;Enter quantity:&quot;" newline="True"/>
                            <input variable="quantity"/>
                            <assign variable="total" expression="quantity * 20"/>
                            <if expression="quantity&lt;0">
                                <then>
                                    <output expression="&quot;You purchased Tea&quot;" newline="True"/>
                                    <output expression="&quot;Total Price : &quot; &amp; total" newline="True"/>
                                    <output expression="&quot;Enjoy!&quot;" newline="True"/>
                                </then>
                                <else>
                                    <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                                </else>
                            </if>
                        </then>
                        <else>
                            <output expression="&quot;invalid menu&quot;" newline="True"/>
                        </else>
                    </if>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>