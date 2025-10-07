<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab.2"/>
        <attribute name="authors" value="Admin"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-17 09:53:38 PM"/>
        <attribute name="created" value="QWRtaW47REVTS1RPUC1GRVNPSFVUOzI1NjgtMDctMTc7MDc6NDQ6MDAgUE07MjkwOQ=="/>
        <attribute name="edited" value="QWRtaW47REVTS1RPUC1GRVNPSFVUOzI1NjgtMDctMTc7MDk6NTM6MzggUE07NzszMDM2"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="c, ct, t, tt, manu, quantity, total" type="Integer" array="False" size=""/>
            <assign variable="c" expression="25"/>
            <assign variable="ct" expression="10"/>
            <assign variable="t" expression="20"/>
            <assign variable="tt" expression="0"/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - &quot;&amp;c&amp;&quot; Baht - Qty: &quot; &amp;ct" newline="True"/>
            <output expression="&quot;2. Tea - &quot;&amp;t&amp;&quot; Baht - Qty: &quot;&amp;tt" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea):&quot;" newline="True"/>
            <input variable="manu"/>
            <output expression="&quot;Enter quantity: &quot;" newline="True"/>
            <input variable="quantity"/>
            <if expression="manu=1">
                <then>
                    <if expression="ct&lt;quantity">
                        <then>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </then>
                        <else>
                            <assign variable="total" expression="c*quantity"/>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <output expression="&quot;Total Price: &quot;&amp;total&amp;&quot; Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <if expression="manu=2">
                        <then>
                            <if expression="tt&lt;quantity">
                                <then>
                                    <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                                </then>
                                <else>
                                    <assign variable="total" expression="t*quantity"/>
                                    <output expression="&quot;You purchased Tea&quot;" newline="True"/>
                                    <output expression="&quot;Total Price: &quot;&amp;total&amp;&quot; Baht&quot;" newline="True"/>
                                    <output expression="&quot;Enjoy!&quot;" newline="True"/>
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