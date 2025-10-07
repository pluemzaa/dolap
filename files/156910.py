<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="2"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 02:41:05 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDI6MTg6NTAgUE07MjU3Nw=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDI6NDE6MDUgUE07MjsyNjgy"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="cof, tea, select, qt" type="Integer" array="False" size=""/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea): &quot;" newline="True"/>
            <input variable="select"/>
            <if expression="select == 1">
                <then>
                    <output expression="&quot;Enter quantity: &quot;" newline="True"/>
                    <input variable="qt"/>
                    <if expression="qt &lt;= 10">
                        <then>
                            <assign variable="cof" expression="25 * qt"/>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <output expression="&quot;Total Price : &quot; &amp; cof &amp; &quot; Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <output expression="&quot;Enter quantity: &quot;" newline="True"/>
                    <input variable="qt"/>
                    <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>