<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="fzz"/>
        <attribute name="authors" value="thasa"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-19 03:02:55 AM"/>
        <attribute name="created" value="dGhhc2E7REVTS1RPUC1DUTY0VDBNOzIwMjUtMDctMTk7MDI6NTM6MzIgQU07Mjg0NQ=="/>
        <attribute name="edited" value="dGhhc2E7REVTS1RPUC1DUTY0VDBNOzIwMjUtMDctMTk7MDM6MDI6NTUgQU07MjsyOTU0"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="c, t, cp, tp, i, n" type="Integer" array="False" size=""/>
            <assign variable="cp" expression="25"/>
            <assign variable="c" expression="10"/>
            <assign variable="tp" expression="20"/>
            <assign variable="t" expression="0"/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty:&quot; &amp;c" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty:&quot; &amp;t" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea):&quot;" newline="True"/>
            <input variable="i"/>
            <if expression="i==1">
                <then>
                    <output expression="&quot;Enter quantity:&quot;" newline="True"/>
                    <input variable="n"/>
                    <if expression="n&lt;=c">
                        <then>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <output expression="&quot;Total Price :&quot; &amp;(n*cp)&amp; &quot;Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <if expression="i==2">
                        <then>
                            <output expression="&quot;Enter quantity:&quot;" newline="True"/>
                            <input variable="n"/>
                            <if expression="n&lt;=t">
                                <then>
                                    <output expression="&quot;You purchased Tea&quot;" newline="True"/>
                                    <output expression="&quot;Total Price :&quot; &amp;(n*tp)&amp; &quot;Baht&quot;" newline="True"/>
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