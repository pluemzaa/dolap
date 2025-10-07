<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="flowchart &#3586;&#3657;&#3629; 2"/>
        <attribute name="authors" value="benzs"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-17 04:13:01 PM"/>
        <attribute name="created" value="YmVuenM7REVTS1RPUC1FNDZHTjZKOzIwMjUtMDctMTc7MDI6NTE6MTAgUE07Mjg1OA=="/>
        <attribute name="edited" value="YmVuenM7REVTS1RPUC1FNDZHTjZKOzIwMjUtMDctMTc7MDQ6MTM6MDEgUE07NDsyOTY5"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="cp, tp, QtyC, QtyT, i, n, Totalcp, Totaltp" type="Real" array="False" size=""/>
            <assign variable="cp" expression="25"/>
            <assign variable="tp" expression="20"/>
            <assign variable="QtyC" expression="10"/>
            <assign variable="QtyT" expression="0"/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea):&quot;" newline="True"/>
            <input variable="i"/>
            <if expression="i==1">
                <then>
                    <output expression="&quot;Enter quantity:&quot;" newline="True"/>
                    <input variable="n"/>
                    <if expression="n&lt;=QtyC">
                        <then>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <assign variable="Totalcp" expression="cp*n"/>
                            <output expression="&quot;Total Price : &quot; &amp; Totalcp &amp; &quot; Baht&quot;" newline="True"/>
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
                            <if expression="n&lt;=QtyT">
                                <then>
                                    <output expression="&quot;You purchased Tea&quot;" newline="True"/>
                                    <assign variable="Totaltp" expression="tp*n"/>
                                    <output expression="&quot;Total Price : &quot; &amp; Totaltp &amp; &quot; Baht&quot;" newline="True"/>
                                    <output expression="&quot;Enjoy!&quot;" newline="True"/>
                                </then>
                                <else>
                                    <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                                </else>
                            </if>
                        </then>
                        <else>
                            <output expression="&quot;invaild input.&quot;" newline="True"/>
                        </else>
                    </if>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>