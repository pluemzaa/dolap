<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="2"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-16 05:55:48 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDQ6MjI6NDggUE07MjU4MQ=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDU6MDc6MTQgUE07NDsyNjg5"/>
        <attribute name="edited" value="VXNlcjtERVNLVE9QLUJSODJGRkw7MjU2OC0wNy0xNjswNTo1NTo0OCBQTTs1OzI4ODY="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="Coffee, Tea, qyt, se" type="Integer" array="False" size=""/>
            <assign variable="Coffee" expression="10"/>
            <assign variable="Tea" expression="0"/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea): &quot;" newline="True"/>
            <input variable="se"/>
            <if expression="se=1">
                <then>
                    <output expression="&quot;Enter quantity: &quot;" newline="True"/>
                    <input variable="qyt"/>
                    <if expression="qyt&lt;=Coffee">
                        <then>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <output expression="&quot;Total Price : &quot; &amp; (25 * qyt)&amp;&quot; Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <output expression="&quot;Enter quantity: &quot;" newline="True"/>
                    <input variable="qyt"/>
                    <if expression="qyt&lt;=Tea">
                        <then>
                            <output expression="&quot;You purchased Tea&quot;" newline="True"/>
                            <output expression="&quot;Total Price : &quot; &amp; (20 * qyt)&amp;&quot; Baht&quot;" newline="True"/>
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