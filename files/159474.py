<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="Test4_2"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-23 08:01:33 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xNzswMzoyNTo1MCBQTTsyNTQ0"/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xNzswMzo0NjoxNCBQTTs1OzI2NTk="/>
        <attribute name="edited" value="VmVlcmFwb2o7REVTS1RPUC1LR0QzVEZSOzIwMjUtMDctMjM7MDg6MDE6MzMgUE07MTszMzAw"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="Drink" type="Integer" array="False" size=""/>
            <declare name="TeaPrice, CoffeePrice" type="Integer" array="False" size=""/>
            <assign variable="TeaPrice" expression="20"/>
            <assign variable="CoffeePrice" expression="25"/>
            <declare name="TeaQuantity, CoffeeQuantity" type="Integer" array="False" size=""/>
            <declare name="TeaOrder, CoffeeOrder" type="Integer" array="False" size=""/>
            <assign variable="TeaQuantity" expression="0"/>
            <assign variable="CoffeeQuantity" expression="10"/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea): &quot;" newline="True"/>
            <input variable="Drink"/>
            <if expression="Drink == 1">
                <then>
                    <output expression="&quot;Enter quantity: &quot;" newline="True"/>
                    <input variable="CoffeeOrder"/>
                    <if expression="CoffeeOrder &gt; CoffeeQuantity">
                        <then>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <output expression="&quot;Total Price : &quot; &amp; CoffeePrice  *  CoffeeOrder &amp; &quot; Baht&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <if expression="Drink == 2">
                        <then>
                            <output expression="&quot;Enter quantity: &quot;" newline="True"/>
                            <input variable="TeaOrder"/>
                            <if expression="TeaOrder &gt; TeaQuantity">
                                <then>
                                    <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                                </then>
                                <else>
                                    <output expression="&quot;You purchased Tea&quot;" newline="True"/>
                                    <output expression="&quot;Total Price : &quot; &amp; TeaPrice  *  TeaOrder &amp;&quot; Baht&quot;" newline="True"/>
                                </else>
                            </if>
                        </then>
                        <else>
                            <output expression="&quot;hmm&quot;" newline="True"/>
                        </else>
                    </if>
                </else>
            </if>
            <output expression="&quot;Enjoy!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>