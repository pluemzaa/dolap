<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="TaoBin_VendingMachine_Corrected"/>
        <attribute name="authors" value="AI Assistant"/>
        <attribute name="about" value="Flowchart &#3626;&#3635;&#3627;&#3621;&#3633;&#3610;&#3605;&#3641;&#3657;&#3585;&#3604;&#3648;&#3588;&#3619;&#3639;&#3656;&#3629;&#3591;&#3648;&#3588;&#3619;&#3639;&#3656;&#3629;&#3591;&#3604;&#3639;&#3656;&#3617;&#3585;&#3619;"/>
        <attribute name="saved" value="2024-07-19 10:00:00 AM"/>
        <attribute name="created" value="QVNVUztMQVBUT1AtTVVIVTVGSEc7MjU2OC0wNy0xOTsxMDowMDowMCBBTTsyNzAx"/>
        <attribute name="edited" value="QVNVUztMQVBUT1AtTVVIVTVGSEc7MjU2OC0wNy0xOTsxMDowMDowMCBBTTs5OzI4MDk="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="menu" type="Integer" array="False" size=""/>
            <declare name="quantity" type="Integer" array="False" size=""/>
            <declare name="totalPrice" type="Integer" array="False" size=""/>
            <declare name="coffeePrice" type="Integer" array="False" size=""/>
            <declare name="coffeeQty" type="Integer" array="False" size=""/>
            <declare name="teaPrice" type="Integer" array="False" size=""/>
            <declare name="teaQty" type="Integer" array="False" size=""/>
            <comment text="&# bước 1: &#3585;&#3635;&#3627;&#3609;&#3604;&#3588;&#3656;&#3634;&#3605;&#3633;&#3623;&#3649;&#3611;&#3619; (Initialize variables)"/>
            <assign variable="coffeePrice" expression="25"/>
            <assign variable="coffeeQty" expression="10"/>
            <assign variable="teaPrice" expression="20"/>
            <assign variable="teaQty" expression="0"/>
            <comment text="&# bước 2: &#3649;&#3626;&#3604;&#3591;&#3648;&#3617;&#3609;&#3641; (Display menu)"/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - &quot; &amp; coffeePrice &amp; &quot; Baht - Qty: &quot; &amp; coffeeQty" newline="True"/>
            <output expression="&quot;2. Tea - &quot; &amp; teaPrice &amp; &quot; Baht - Qty: &quot; &amp; teaQty" newline="True"/>
            <comment text="&# bước 3: &#3619;&#3633;&#3610;&#3586;&#3657;&#3629;&#3617;&#3641;&#3621;&#3634;&#3585;&#3634;&#3619;&#3626;&#3633;&#3656;&#3591;&#3592;&#3634;&#3585; (Get user input)"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea):&quot;" newline="True"/>
            <input variable="menu"/>
            <if expression="menu == 1">
                <then>
                    <comment text="&#3611;&#3619;&#3632;&#3649;&#3585;&#3619;&#3603;&#3637;&#3648;&#3621;&#3639;&#3629;&#3585;&#3634;&#3649;&#3615; (Coffee logic)"/>
                    <if expression="coffeeQty > 0">
                        <then>
                            <output expression="&quot;Enter quantity:&quot;" newline="True"/>
                            <input variable="quantity"/>
                            <if expression="quantity &lt;= coffeeQty">
                                <then>
                                    <assign variable="totalPrice" expression="quantity * coffeePrice"/>
                                    <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                                    <output expression="&quot;Total Price : &quot; &amp; totalPrice &amp; &quot; Baht&quot;" newline="True"/>
                                    <output expression="&quot;Enjoy!&quot;" newline="True"/>
                                </then>
                                <else>
                                    <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                                </else>
                            </if>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <if expression="menu == 2">
                        <then>
                            <comment text="&#3611;&#3619;&#3632;&#3649;&#3585;&#3619;&#3603;&#3637;&#3648;&#3621;&#3639;&#3629;&#3585;&#3634; (Tea logic)"/>
                            <if expression="teaQty > 0">
                                <then>
                                    <output expression="&quot;Enter quantity:&quot;" newline="True"/>
                                    <input variable="quantity"/>
                                    <if expression="quantity &lt;= teaQty">
                                        <then>
                                            <assign variable="totalPrice" expression="quantity * teaPrice"/>
                                            <output expression="&quot;You purchased Tea&quot;" newline="True"/>
                                            <output expression="&quot;Total Price : &quot; &amp; totalPrice &amp; &quot; Baht&quot;" newline="True"/>
                                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                                        </then>
                                        <else>
                                            <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                                        </else>
                                    </if>
                                </then>
                                <else>
                                    <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                                </else>
                            </if>
                        </then>
                        <else>
                            <comment text="&#3585;&#3619;&#3603;&#3637;&#3648;&#3621;&#3639;&#3629;&#3585;&#3648;&#3617;&#3609;&#3641;&#3652;&#3617;&#3656;&#3606;&#3641;&#3585;&#3605;&#3657;&#3629;&#3591; (Invalid menu choice)"/>
                            <output expression="&quot;Invalid menu selection.&quot;" newline="True"/>
                        </else>
                    </if>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>