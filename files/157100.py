<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="t2"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 04:54:50 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDQ6MzU6MDcgUE07MjU4MA=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDQ6NTQ6NTAgUE07MjsyNjg4"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="se, qu, co, t" type="Integer" array="False" size=""/>
            <assign variable="t" expression="0"/>
            <assign variable="co" expression="10"/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea): &quot;" newline="True"/>
            <input variable="se"/>
            <if expression="se=1">
                <then>
                    <output expression="&quot;Enter quantity: &quot;" newline="True"/>
                    <input variable="qu"/>
                    <if expression="qu&lt;=10">
                        <then>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <output expression="&quot;Total Price :&quot;&amp;(qu*25)&amp; &quot;Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <output expression="&quot;Enter quantity: &quot;" newline="True"/>
                    <input variable="qu"/>
                    <if expression="qu&lt;=0">
                        <then>
                            <output expression="&quot;You purchased Tea&quot;" newline="True"/>
                            <output expression="&quot;Total Price :&quot;&amp;(qu*20)&amp; &quot;Baht&quot;" newline="True"/>
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