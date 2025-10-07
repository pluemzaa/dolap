<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="Lab4_2"/>
        <attribute name="authors" value="bizr"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-20 08:55:41 "/>
        <attribute name="created" value="Yml6cjtNQUNCT09LQUlSOzI1NjgtMDctMTk7IjA5OjEzOjQ1ICI7MjM4Mg=="/>
        <attribute name="edited" value="Yml6cjtNQUNCT09LQUlSOzI1NjgtMDctMjA7IjA4OjU1OjQxICI7ODsyNDkw"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="coffeeQty, coffeePrice, menu, total" type="Integer" array="False" size=""/>
            <assign variable="coffeeQty" expression="10"/>
            <assign variable="coffeePrice" expression="25"/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea):&quot;" newline="True"/>
            <input variable="menu"/>
            <output expression="&quot;Enter quantity:&quot;" newline="True"/>
            <input variable="coffeeQty"/>
            <assign variable="total" expression="coffeeQty*coffeePrice"/>
            <if expression="menu == 1">
                <then>
                    <if expression="coffeeQty&lt;=10">
                        <then>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <output expression="&quot;Total Price :&quot;&amp;total&amp; &quot;Baht&quot;" newline="True"/>
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