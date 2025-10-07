<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4.RabbitVender"/>
        <attribute name="authors" value="akung"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-17 05:30:38 PM"/>
        <attribute name="created" value="YWt1bmc7S0lERE87MjU2OC0wNy0xNzswNDo1NDoyNCBQTTsyMTk2"/>
        <attribute name="edited" value="YWt1bmc7S0lERE87MjU2OC0wNy0xNzswNTozMDozOCBQTTsxMjsyMzU0"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="qcof, qtea, pcof, ptea, total, menu, qty" type="Integer" array="False" size=""/>
            <assign variable="qcof" expression="10"/>
            <assign variable="qtea" expression="0"/>
            <assign variable="pcof" expression="25"/>
            <assign variable="ptea" expression="20"/>
            <output expression="&quot;Beverage List: &quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10 &quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0 &quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea):&quot;" newline="True"/>
            <input variable="menu"/>
            <output expression="&quot;Enter quantity: &quot;" newline="True"/>
            <input variable="qty"/>
            <if expression="menu == 1">
                <then>
                    <if expression="qty &lt;= qcof">
                        <then>
                            <assign variable="total" expression="qty*pcof"/>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <output expression="&quot;Total Price : &quot; &amp;total&amp; &quot; Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <if expression="menu == 2">
                        <then>
                            <if expression="qty &lt;= qtea">
                                <then/>
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