<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_2"/>
        <attribute name="authors" value="Lenovo"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-19 10:54:17 PM"/>
        <attribute name="created" value="TGVub3ZvO0xBUFRPUC1GMk9BVDRQSTsyNTY4LTA3LTE5OzA5OjAyOjIwIFBNOzI5ODQ="/>
        <attribute name="edited" value="TGVub3ZvO0xBUFRPUC1GMk9BVDRQSTsyNTY4LTA3LTE5OzEwOjU0OjE3IFBNOzE7MzA5Nw=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="name" type="String" array="True" size="2"/>
            <declare name="price" type="Integer" array="True" size="2"/>
            <declare name="quantity" type="Integer" array="True" size="2"/>
            <declare name="total, menu, order" type="Integer" array="False" size=""/>
            <assign variable="name[0]" expression="&quot;Coffee&quot;"/>
            <assign variable="name[1]" expression="&quot;Tea&quot;"/>
            <assign variable="price[0]" expression="25"/>
            <assign variable="price[1]" expression="20"/>
            <assign variable="quantity[0]" expression="10"/>
            <assign variable="quantity[1]" expression="0"/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea): &quot;" newline="True"/>
            <input variable="menu"/>
            <output expression="&quot;Enter quantity: &quot;" newline="True"/>
            <input variable="order"/>
            <if expression="order&gt;quantity[menu-1]">
                <then>
                    <output expression="&quot;Sorry, &quot; &amp; name[menu-1] &amp; &quot; out of stock&quot;" newline="True"/>
                </then>
                <else>
                    <assign variable="total" expression="order*price[menu-1]"/>
                    <output expression="&quot;You purchased &quot; &amp;name[menu-1]" newline="True"/>
                    <output expression="&quot;Total Price : &quot; &amp;total&amp; &quot; Baht&quot;" newline="True"/>
                    <output expression="&quot;Enjoy!&quot;" newline="True"/>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>