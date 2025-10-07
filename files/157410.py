<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="2"/>
        <attribute name="authors" value="Windows10"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-19 12:55:20 PM"/>
        <attribute name="created" value="V2luZG93czEwO0RFU0tUT1AtSEpRNVVTQTsyNTY4LTA3LTE3OzA4OjU0OjUzIFBNOzMyNDU="/>
        <attribute name="edited" value="V2luZG93czEwO0RFU0tUT1AtSEpRNVVTQTsyNTY4LTA3LTE5OzEyOjU1OjIwIFBNOzEzOzMzOTY="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="menu" type="Integer" array="False" size=""/>
            <declare name="Coffe, Tea, Total, quantity, quantityCoffe, quantityTea" type="Integer" array="False" size=""/>
            <assign variable="total" expression="0"/>
            <assign variable="Coffe" expression="25"/>
            <assign variable="Tea" expression="20"/>
            <assign variable="quantityCoffe" expression="10"/>
            <assign variable="quantityTea" expression="0"/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <input variable="menu"/>
            <if expression="menu==1">
                <then>
                    <output expression="&quot;Select menu (1 = Coffee, 2 = Tea): &quot;" newline="True"/>
                    <output expression="&quot;Enter quantity:&quot;" newline="True"/>
                    <input variable="quantityCoffe"/>
                    <if expression="quantityCoffe&lt;=10">
                        <then>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <assign variable="total" expression="Coffe*quantityCoffe"/>
                            <output expression="&quot;Total Price :&quot;&amp; total &amp;&quot; Baht&quot;" newline="True"/>
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
                            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea): &quot;" newline="True"/>
                            <output expression="&quot;Enter quantity:&quot;" newline="True"/>
                            <input variable="quantityTea"/>
                            <if expression="quantityTea&lt;0">
                                <then>
                                    <output expression="&quot;You purchased Tea&quot;" newline="True"/>
                                    <assign variable="total" expression="Tea*quantityTea"/>
                                    <output expression="&quot;Total Price :&quot;&amp; total &amp;&quot; Baht&quot;" newline="True"/>
                                    <output expression="&quot;Enjoy!&quot;" newline="True"/>
                                </then>
                                <else>
                                    <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
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