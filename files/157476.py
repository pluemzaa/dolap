<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="finish 2"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-22 01:05:10 AM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDY6MjQ6MjcgUE07MjU4Mg=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDc6MTA6NDYgUE07MTtjb21wdXRlcjtDUC1DT007MjAyNS0wNy0xNjswNTo0OTozMSBQTTtsYWIgNCBfMSBmaW5pc2guZnByZzs3MTAx"/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDc6MjA6MzQgUE07MTsyNjg1"/>
        <attribute name="edited" value="VXNlcjtKRVM7MjU2OC0wNy0yMjswMTowNToxMCBBTTs5OzIwMjU="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="Menu, Coffee, Tea, Qty1, Qty2" type="Integer" array="False" size=""/>
            <assign variable="Coffee" expression="25"/>
            <assign variable="Qty1" expression="10"/>
            <assign variable="Tea" expression="20"/>
            <assign variable="Qty2" expression="0"/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <output expression="&quot;Select menu&quot;" newline="True"/>
            <output expression="&quot;1 = Coffee, 2 = Tea&quot;" newline="True"/>
            <input variable="Menu"/>
            <if expression="Menu==1">
                <then>
                    <output expression="&quot;Enter quantity:&quot;" newline="True"/>
                    <input variable="Qty1"/>
                    <if expression="Qty1&lt;=10">
                        <then>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <output expression="&quot;Total Price : &quot;&amp; (Coffee*Qty1) &amp; &quot; Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <if expression="Menu==2">
                        <then>
                            <output expression="&quot;Enter quantity:&quot;" newline="True"/>
                            <input variable="Qty2"/>
                            <if expression="Qty2 &lt; 0">
                                <then>
                                    <output expression="&quot;You purchased Tea&quot;" newline="True"/>
                                    <output expression="&quot;Total Price : &quot; &amp; (Tea*Qty2)" newline="True"/>
                                    <output expression="&quot;Enjoy!&quot;" newline="True"/>
                                </then>
                                <else>
                                    <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                                </else>
                            </if>
                        </then>
                        <else>
                            <output expression="&quot;Sorry,Dont have menu&quot;" newline="True"/>
                        </else>
                    </if>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>