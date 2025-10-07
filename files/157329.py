<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="loop_2"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-17 04:00:26 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xNzswMjo0MTo0MSBQTTsyNTQx"/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xNzswMjo0MTo1NiBQTTsyO2NvbXB1dGVyO0NQQ09NOzI1NjgtMDctMTc7MDI6MzI6MDQgUE07bG9vcC5mcHJnOzYyMzM="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xNzswNDowMDoyNiBQTTszOzI2NTE="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, interest" type="Real" array="False" size=""/>
            <declare name="year, i" type="Integer" array="False" size=""/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="year"/>
            <assign variable="i" expression="0"/>
            <while expression="i &lt; year">
                <assign variable="money" expression="money * (1 +(interest / 100))"/>
                <assign variable="i" expression="i+1"/>
                <output expression="&quot;year  &quot;&amp;i &amp; &quot;:&quot; &amp; money" newline="True"/>
            </while>
        </body>
    </function>
</flowgorithm>