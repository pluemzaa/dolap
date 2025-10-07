<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="Dolab4_2"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 06:50:28 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDY6MTQ6MDEgUE07MjU3Mw=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDY6NTA6MjggUE07MTsyNjkw"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="Coffeequantity, Teaquantity, menu, Coffeeprice, Teaprice, quantity, total" type="Integer" array="False" size=""/>
            <assign variable="Coffeequantity" expression="10"/>
            <assign variable="Teaquantity" expression="0"/>
            <assign variable="Teaprice" expression="20"/>
            <assign variable="Coffeeprice" expression="25"/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - &quot;&amp;Coffeeprice&amp;&quot; Baht - Qty: &quot;&amp;Coffeequantity" newline="True"/>
            <output expression="&quot;2. Tea - &quot;&amp;Teaprice&amp;&quot; Baht - Qty: &quot; &amp; Teaquantity" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea):&quot;" newline="True"/>
            <input variable="menu"/>
            <output expression="&quot;Enter quantity: &quot;" newline="True"/>
            <input variable="quantity"/>
            <if expression="menu=1">
                <then>
                    <if expression="Coffeequantity&lt;quantity">
                        <then>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </then>
                        <else>
                            <assign variable="total" expression="Coffeeprice*quantity"/>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <output expression="&quot;Total Price : &quot;&amp;total&amp;&quot; Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <if expression="menu=2">
                        <then>
                            <if expression="Teaquantity&lt;quantity">
                                <then>
                                    <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                                </then>
                                <else>
                                    <assign variable="total" expression="Teaprice*quantity"/>
                                    <output expression="&quot;You purchased Tea&quot;" newline="True"/>
                                    <output expression="&quot;Total Price : &quot;&amp;total&amp;&quot; Baht&quot;" newline="True"/>
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