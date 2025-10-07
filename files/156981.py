<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_2"/>
        <attribute name="authors" value="MyPC"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-22 02:30:13 AM"/>
        <attribute name="created" value="TXlQQztERVNLVE9QLTZHQkE3MEk7MjAyNS0wNy0yMTsxMToxMzozNCBQTTsyNjM2"/>
        <attribute name="edited" value="TXlQQztERVNLVE9QLTZHQkE3MEk7MjAyNS0wNy0yMjswMjozMDoxMyBBTTszOzI3Mjg="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="c, t, cq, tq, cp, tp, cn, tn, m" type="Integer" array="False" size=""/>
            <assign variable="cq" expression="10"/>
            <assign variable="tq" expression="0"/>
            <assign variable="cp" expression="25"/>
            <assign variable="tp" expression="20"/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - &quot; &amp; cp &amp; &quot;Baht - Qty: &quot; &amp; cq" newline="True"/>
            <output expression="&quot;2. Tea - &quot; &amp; tp &amp; &quot;Baht - Qty: &quot; &amp; tq" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea):&quot;" newline="True"/>
            <input variable="m"/>
            <if expression="m=1">
                <then>
                    <output expression="&quot;Enter quantity: &quot;" newline="True"/>
                    <input variable="cn"/>
                    <if expression="cn&lt;=cq">
                        <then>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <output expression="&quot;Total Price : &quot; &amp; cn*cp &amp; &quot;Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <if expression="m=2">
                        <then>
                            <output expression="&quot;Enter quantity: &quot;" newline="True"/>
                            <input variable="tn"/>
                            <if expression="tn&lt;=tq">
                                <then>
                                    <output expression="&quot;You purchased Tea&quot;" newline="True"/>
                                    <output expression="&quot;Total Price : &quot; &amp; tn*tp &amp; &quot;Baht&quot;" newline="True"/>
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