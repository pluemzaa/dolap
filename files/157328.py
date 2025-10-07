<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="003"/>
        <attribute name="authors" value="USER"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-17 03:57:23 PM"/>
        <attribute name="created" value="VVNFUjtERVNLVE9QLVBQREtFMUk7MjAyNS0wNy0xNzswMzozNTo0OCBQTTsyNjg3"/>
        <attribute name="edited" value="VVNFUjtERVNLVE9QLVBQREtFMUk7MjAyNS0wNy0xNzswMzo1NzoyMyBQTTsxOzI3OTI="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, dok, pe, i" type="Integer" array="False" size=""/>
            <declare name="y" type="Real" array="False" size=""/>
            <assign variable="i" expression="0"/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="money"/>
            <assign variable="y" expression="money"/>
            <output expression="&quot;Input interest (%):&quot;" newline="True"/>
            <input variable="dok"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="pe"/>
            <while expression="i&lt;pe">
                <assign variable="y" expression="y*(1+dok/100)"/>
                <output expression="&quot;Year&quot; &amp; (i+1) &amp; &quot;:&quot; &amp; y" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>