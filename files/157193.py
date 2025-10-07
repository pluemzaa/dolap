<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="2"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 06:56:31 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDY6Mjk6MzcgUE07MjU4OA=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDY6NDk6NDUgUE07Mjtjb21wdXRlcjtDUC1DT007MjAyNS0wNy0xNjswNTo1NzozNCBQTTsxLmZwcmc7NTkyNw=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDY6NTY6MzEgUE07MjsyNjkx"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="menu, qty, total" type="Integer" array="False" size=""/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea): &quot;" newline="True"/>
            <input variable="menu"/>
            <output expression="&quot;Enter quantity: &quot;" newline="True"/>
            <input variable="qty"/>
            <if expression="menu == 1">
                <then>
                    <if expression="qty &lt;= 10">
                        <then>
                            <assign variable="total" expression="qty * 25"/>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <output expression="&quot;Total Price : &quot; &amp; total &amp; &quot; Baht &quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock &quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <if expression="menu == 2">
                        <then>
                            <output expression="&quot;Sorry, Tea out of stock &quot;" newline="True"/>
                        </then>
                        <else/>
                    </if>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>