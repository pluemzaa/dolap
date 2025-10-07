<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="TOOD2"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 04:37:41 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDQ6MTU6MTYgUE07MjU3OA=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDQ6Mzc6NDEgUE07MzsyNjkw"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="Coffee" type="Integer" array="False" size=""/>
            <declare name="Tea" type="Integer" array="False" size=""/>
            <assign variable="Coffee" expression="10"/>
            <assign variable="Tea" expression="0"/>
            <declare name="menu" type="Integer" array="False" size=""/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea): &quot;" newline="True"/>
            <input variable="menu"/>
            <if expression="menu == 1">
                <then>
                    <declare name="Coffeeprice" type="Integer" array="False" size=""/>
                    <declare name="nCoffee" type="Integer" array="False" size=""/>
                    <output expression="&quot;Enter quantity: &quot;" newline="True"/>
                    <input variable="nCoffee"/>
                    <if expression="(10 - ncoffee)&gt;=0">
                        <then>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <assign variable="Coffeeprice" expression="nCoffee*25"/>
                            <output expression="&quot;Total Price : &quot; &amp; Coffeeprice &amp; &quot;Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <declare name="atea" type="Integer" array="False" size=""/>
                    <declare name="ntea" type="Integer" array="False" size=""/>
                    <output expression="&quot;Enter quantity: &quot;" newline="True"/>
                    <input variable="ntea"/>
                    <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>