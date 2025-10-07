<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_2"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-20 05:33:47 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDQ6MjQ6MDEgUE07MjU3Mg=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDU6MDE6MjIgUE07NjsyNjg0"/>
        <attribute name="edited" value="VXNlcjtERVNLVE9QLURLTjQyRUM7MjAyNS0wNy0yMDswNTozMzo0NyBQTTsyOzI4NTA="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="coffee, tea, menu, Total" type="Integer" array="False" size=""/>
            <declare name="teaprice" type="Real" array="False" size=""/>
            <assign variable="teaprice" expression="20"/>
            <declare name="coffeeprice" type="Real" array="False" size=""/>
            <assign variable="coffeeprice" expression="25"/>
            <declare name="qc, qt" type="Real" array="False" size=""/>
            <assign variable="qc" expression="10"/>
            <assign variable="qt" expression="0"/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea):&quot;" newline="True"/>
            <input variable="menu"/>
            <output expression="&quot;Enter quantity: &quot;" newline="True"/>
            <if expression="menu==1">
                <then>
                    <input variable="qc"/>
                    <if expression="qc&lt;=10">
                        <then>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                    <assign variable="Total" expression="(coffeeprice*qc)"/>
                    <output expression="&quot;Total Price :&quot;&amp;Total" newline="True"/>
                    <output expression="&quot;Enjoy!&quot;" newline="True"/>
                </then>
                <else>
                    <if expression="menu==2">
                        <then>
                            <input variable="qt"/>
                            <if expression="qt &gt; 0">
                                <then>
                                    <output expression="&quot;Sorry, tea out of stock&quot;" newline="True"/>
                                </then>
                                <else>
                                    <output expression="&quot;Sorry, tea out of stock&quot;" newline="True"/>
                                </else>
                            </if>
                        </then>
                        <else>
                            <output expression="&quot;Invalide number&quot;" newline="True"/>
                        </else>
                    </if>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>