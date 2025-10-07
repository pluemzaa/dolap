<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="coffeeshop"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 07:02:49 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDU6MzQ6MDQgUE07MjU3Nw=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDc6MDI6NDkgUE07MjsyNjky"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <declare name="Coffee, Tea, calculation, Teacal" type="Integer" array="False" size=""/>
            <assign variable="Coffee" expression="25"/>
            <assign variable="Tea" expression="20"/>
            <declare name="QtyC, n, QtyT" type="Integer" array="False" size=""/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea): &quot;" newline="True"/>
            <input variable="n"/>
            <if expression="n == 1">
                <then>
                    <output expression="&quot;Enter quantity:&quot;" newline="True"/>
                    <input variable="QtyC"/>
                    <if expression="QtyC &lt;= 10">
                        <then>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <assign variable="calculation" expression="QtyC * Coffee"/>
                            <output expression="&quot;Total Price : &quot; &amp;calculation&amp; &quot; Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <if expression="n == 2">
                        <then>
                            <output expression="&quot;Enter quantity:&quot;" newline="True"/>
                            <input variable="QtyT"/>
                            <if expression="QtyT == 0">
                                <then>
                                    <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                                    <assign variable="Teacal" expression="QtyT*Tea"/>
                                </then>
                                <else>
                                    <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                                </else>
                            </if>
                        </then>
                        <else>
                            <output expression="&quot;invalid&quot;" newline="True"/>
                        </else>
                    </if>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>