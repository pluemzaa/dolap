<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="coffeetea"/>
        <attribute name="authors" value="Theerapong-PC01"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-16 06:48:43 PM"/>
        <attribute name="created" value="VGhlZXJhcG9uZy1QQzAxO0RFU0tUT1AtVFFCNTFHRTsyNTY4LTA3LTE2OzA2OjMyOjQ1IFBNOzM2ODE="/>
        <attribute name="edited" value="VGhlZXJhcG9uZy1QQzAxO0RFU0tUT1AtVFFCNTFHRTsyNTY4LTA3LTE2OzA2OjQ4OjQzIFBNOzI7Mzc5NQ=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="CoffeeQty, TeaQty, menu, qty" type="Integer" array="False" size=""/>
            <declare name="CoffeePrice, TeaPrice" type="Real" array="False" size=""/>
            <assign variable="CoffeePrice" expression="25"/>
            <assign variable="TeaPrice" expression="20"/>
            <assign variable="CoffeeQty" expression="10"/>
            <assign variable="TeaQty" expression="0"/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1)Coffee-&quot; &amp; CoffeePrice &amp; &quot;Baht-Qty:&quot; &amp; CoffeeQty" newline="True"/>
            <output expression="&quot;1)Tea-&quot; &amp; TeaPrice &amp; &quot;Baht-Qty:&quot; &amp; TeaQty" newline="True"/>
            <output expression="&quot;Select menu (1=Coffee, 2=Tea):&quot;" newline="True"/>
            <input variable="menu"/>
            <output expression="&quot;Enter quantity:&quot;" newline="True"/>
            <input variable="Qty"/>
            <if expression="menu==1">
                <then>
                    <if expression="CoffeeQty &gt;= Qty">
                        <then>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <output expression="&quot;Total Price:&quot; &amp; (CoffeePrice*Qty) &amp; &quot;Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry,Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <if expression="menu==2">
                        <then>
                            <if expression="TeaQty &gt;= Qty">
                                <then>
                                    <output expression="&quot;You purchased Tea&quot;" newline="True"/>
                                    <output expression="&quot;Total Price:&quot; &amp; (TeaPrice*Qty) &amp; &quot;Baht&quot;" newline="True"/>
                                    <output expression="&quot;Enjoy!&quot;" newline="True"/>
                                </then>
                                <else>
                                    <output expression="&quot;Sorry,Tea out of stock&quot;" newline="True"/>
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