<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="kklo"/>
        <attribute name="authors" value="User"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-18 02:42:05 AM"/>
        <attribute name="created" value="VXNlcjtERVNLVE9QLTNJQ0g4UUk7MjU2OC0wNy0xODswMjoxMDoxNiBBTTsyNzQ3"/>
        <attribute name="edited" value="VXNlcjtERVNLVE9QLTNJQ0g4UUk7MjU2OC0wNy0xODswMjo0MjowNSBBTTsxOzI4NTg="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="mon" type="Real" array="False" size=""/>
            <declare name="inter" type="Real" array="False" size=""/>
            <declare name="year" type="Real" array="False" size=""/>
            <declare name="yearco" type="Real" array="False" size=""/>
            <declare name="amo" type="Real" array="False" size=""/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="mon"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="inter"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="year"/>
            <assign variable="yearco" expression="1"/>
            <assign variable="amo" expression="mon"/>
            <while expression="yearco&lt;=year">
                <assign variable="amo" expression="amo*(1+(inter/100))"/>
                <output expression="&quot;year &quot;&amp;yearco&amp;&quot;:&quot;&amp;amo" newline="True"/>
                <assign variable="yearco" expression="yearco+1"/>
            </while>
        </body>
    </function>
</flowgorithm>